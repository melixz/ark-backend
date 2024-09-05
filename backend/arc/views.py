from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import City
from .serializers import FullResponseSerializer, DynamicFormSubmissionSerializer


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
    def post(self, request, *args, **kwargs):
        serializer = DynamicFormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Форма успешно отправлена"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
