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

    @swagger_auto_schema(
        operation_description="Прием данных динамической формы, отправка в CRM и Telegram.",
        responses={status.HTTP_201_CREATED: DynamicFormSubmissionSerializer},
    )
    def post(self, request, format=None):
        data = request.data

        # 1. Сохранение данных формы в базу данных
        form_submission = DynamicFormSubmission(
            name="Dynamic Form Submission",  # Можно настроить для динамической передачи названия формы
            data=data,  # Данные формы сохраняем как JSON
        )
        form_submission.save()

        # Сериализация данных для ответа
        serializer = DynamicFormSubmissionSerializer(form_submission)

        # 2. Подготовка данных для отправки в CRM API
        crm_api_url = "https://ark.yucrm.ru/api/orders/post"
        crm_api_token = settings.CRM_API_TOKEN  # Токен API для CRM, хранимый в .env

        crm_data = {
            "oauth_token": crm_api_token,
            "name": data.get("name", "Не указано"),  # Получаем имя клиента
            "phone": data.get("phone", ""),  # Телефон клиента
            "email": data.get("email", ""),  # Email клиента
            "message": data.get("message", ""),  # Сообщение клиента, если есть
            "referrer": request.META.get("HTTP_REFERER", "Неизвестно"),  # Источник
            "ip": request.META.get("REMOTE_ADDR", "127.0.0.1"),  # IP-адрес клиента
        }

        # Проверка обязательных полей
        if not crm_data["name"] or not crm_data["phone"] or not crm_data["email"]:
            return Response(
                {
                    "error": "Необходимо указать хотя бы одно из полей: name, phone или email"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        headers = {
            "Content-Type": "application/json",
        }

        # 3. Отправка данных на CRM
        try:
            crm_response = requests.post(crm_api_url, json=crm_data, headers=headers)
            if crm_response.status_code == 200:
                crm_response_data = crm_response.json()
            else:
                return Response(
                    {"error": "Ошибка при отправке данных на CRM"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # 4. Получение ID заявки из CRM
        application_id = crm_response_data.get("result", {}).get("id", "Неизвестный ID")

        # 5. Подготовка сообщения для Telegram
        telegram_message = f"""
        Внимание!
        Поступила новая заявка с сайта arkcrimea.ru.
        ID заявки: {application_id}
        Имя: {crm_data['name']}
        Телефон: {crm_data['phone']}
        Почта: {crm_data['email']}
        Ссылка: {crm_data['referrer']}
        """

        # 6. Отправка сообщения в Telegram
        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID

        telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        telegram_data = {"chat_id": chat_id, "text": telegram_message}

        try:
            telegram_response = requests.post(telegram_url, data=telegram_data)
            if telegram_response.status_code != 200:
                return Response(
                    {"error": "Ошибка при отправке сообщения в Telegram"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # 7. Возвращаем успешный ответ
        return Response(serializer.data, status=status.HTTP_201_CREATED)
