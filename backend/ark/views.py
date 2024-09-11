from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City, DynamicFormSubmission
from .serializers import FullResponseSerializer, DynamicFormSubmissionSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class FullDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        new_cities = City.objects.filter(new_title__isnull=False)

        plot_cities = City.objects.filter(plot_title__isnull=False)

        response_data = {
            "new": new_cities,
            "plots": plot_cities,
        }

        serializer = FullResponseSerializer(response_data, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class DynamicFormSubmissionView(APIView):
    class DynamicFormSubmissionView(APIView):
        throttle_classes = [AnonRateThrottle, UserRateThrottle]
        throttle_anon = '100/day'  # 100 запросов в день для анонимных пользователей
        # throttle_user = '1000/day'  # 1000 запросов в день для авторизованных пользователей

    def post(self, request, format=None):
        data = request.data

        form_submission = DynamicFormSubmission(
            name="Dynamic Form Submission", data=data
        )
        form_submission.save()

        serializer = DynamicFormSubmissionSerializer(form_submission)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
