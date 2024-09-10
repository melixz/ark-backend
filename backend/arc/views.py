from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .models import City, DynamicFormSubmission
from .serializers import FullResponseSerializer, DynamicFormSubmissionSerializer


class FullDataAPIView(APIView):
    permission_classes = [IsAdminUser]

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
    permission_classes = [IsAdminUser]

    def post(self, request, format=None):
        data = request.data

        form_submission = DynamicFormSubmission(
            name="Dynamic Form Submission", data=data
        )
        form_submission.save()

        serializer = DynamicFormSubmissionSerializer(form_submission)
        return Response(serializer.data, status=status.HTTP_201_CREATED)