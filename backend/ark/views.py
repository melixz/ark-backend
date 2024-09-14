from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City, DynamicFormSubmission
from .serializers import FullResponseSerializer, DynamicFormSubmissionSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.core.cache import cache


# Кастомные классы для ограничения скорости запросов
class CustomAnonRateThrottle(AnonRateThrottle):
    rate = "100/day"


class CustomUserRateThrottle(UserRateThrottle):
    rate = "1000/day"


class FullDataAPIView(APIView):
    """
    API-представление для получения полной информации о новостройках и застройках.
    """

    permission_classes = [permissions.AllowAny]

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
    API-представление для приема отправок динамических форм.
    """

    def post(self, request, format=None):
        data = request.data

        form_submission = DynamicFormSubmission(
            name="Dynamic Form Submission", data=data
        )
        form_submission.save()

        serializer = DynamicFormSubmissionSerializer(form_submission)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
