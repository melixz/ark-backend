import logging
import requests
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
from django.core.cache import cache
from .models import City, DynamicFormSubmission
from .serializers import FullResponseSerializer, DynamicFormSubmissionSerializer

logger = logging.getLogger(__name__)


# Кастомные классы для ограничения скорости запросов
class CustomAnonRateThrottle(AnonRateThrottle):
    rate = "100/day"


class CustomUserRateThrottle(UserRateThrottle):
    rate = "1000/day"


class FullDataAPIView(ListAPIView):
    """
    API-представление для получения полной информации о новостройках и застройках.
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="Получить полную информацию о новостройках и застройках",
        responses={status.HTTP_200_OK: FullResponseSerializer},
    )
    def get(self, request, *args, **kwargs):
        cache_key = "full_data_api_response"
        data = cache.get(cache_key)

        if not data:
            # Оптимизированные запросы с использованием prefetch_related
            new_cities = City.objects.filter(new_title__isnull=False).prefetch_related(
                "complexes__apartments__sections",
                "complexes__images",
                "new_sections",
                "complexes__apartments__images",
            )

            plot_cities = City.objects.filter(
                plot_title__isnull=False
            ).prefetch_related(
                "plots__lands__sections",
                "plots__images",
                "plot_sections",
                "plots__lands__images",
            )

            response_data = {
                "new": new_cities,
                "plots": plot_cities,
            }

            serializer = FullResponseSerializer(
                response_data, context={"request": request}
            )
            data = serializer.data
            cache.set(cache_key, data, 60 * 15)  # Кэшируем на 15 минут

        return Response(data, status=status.HTTP_200_OK)


class DynamicFormSubmissionView(APIView):
    """
    API-представление для приема отправок динамических форм, отправки данных на CRM и уведомлений в Telegram.
    """

    def post(self, request, format=None):
        data = request.data
        logger.debug(f"Получены данные формы: {data}")

        # 1. Сохранение данных формы в базу данных
        form_submission = DynamicFormSubmission(
            name="Dynamic Form Submission",
            data=data,
        )
        form_submission.save()

        # Сериализация данных для ответа
        serializer = DynamicFormSubmissionSerializer(form_submission)

        # 2. Подготовка данных для отправки в CRM API
        crm_api_url = "https://ark.yucrm.ru/api/orders/post?oauth_token=db261d739af48b5089afa551226ec0b7"

        crm_data = {
            "name": data.get("name", "Не указано"),  # Получаем имя клиента
            "phone": data.get("phone", ""),  # Телефон клиента
            "email": data.get("email", ""),  # Email клиента
            "url": data.get(
                "referrer", "Неизвестно"
            ),  # Получаем переданную ссылку с фронтенда
        }

        logger.debug(f"Отправляем данные в CRM: {crm_data}")

        # 3. Отправка данных на CRM
        try:
            crm_response = requests.post(crm_api_url, data=crm_data)

            # Проверка ответа от CRM
            if crm_response.status_code != 200:
                crm_error_data = crm_response.json()
                logger.error(f"CRM Server error: {crm_error_data}")
                return Response(
                    {
                        "error": f"Ошибка при отправке данных на CRM: {crm_error_data.get('error', {}).get('message', 'Неизвестная ошибка')}"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            else:
                crm_response_data = crm_response.json()
                logger.debug(f"Полный ответ от CRM: {crm_response_data}")

                # Получение ID заявки из CRM
                application_id = crm_response_data.get("result", {}).get(
                    "id", "Неизвестный ID"
                )
                logger.debug(f"ID заявки: {application_id}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при отправке данных в CRM: {e}")
            return Response(
                {"error": f"Ошибка при отправке формы в CRM: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # 4. Подготовка сообщения для Telegram
        telegram_message = (
            "Внимание!\n"
            "Поступила новая заявка с сайта arkcrimea.ru.\n"
            f"ID заявки: {application_id}\n"
            f"Имя: {crm_data['name']}\n"
            f"Телефон: {crm_data['phone']}\n"
            f"Почта: {crm_data['email']}\n"
            f"Ссылка: {crm_data['url']}\n"
        )

        logger.debug(f"Отправляем сообщение в Telegram: {telegram_message}")

        # 5. Отправка сообщения в Telegram
        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID

        telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        telegram_data = {"chat_id": chat_id, "text": telegram_message}

        try:
            telegram_response = requests.post(telegram_url, data=telegram_data)
            logger.debug(
                f"Ответ от Telegram: {telegram_response.status_code}, {telegram_response.text}"
            )
            if telegram_response.status_code != 200:
                return Response(
                    {"error": "Ошибка при отправке сообщения в Telegram"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при отправке данных в Telegram: {e}")
            return Response(
                {"error": f"Ошибка при отправке сообщения в Telegram: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # 6. Возвращаем успешный ответ с данными формы
        return Response(serializer.data, status=status.HTTP_201_CREATED)
