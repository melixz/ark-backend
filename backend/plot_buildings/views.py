from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import PlotBuilding
from .serializers import PlotBuildingSerializer
from main_page.models import Header, Footer, ContactForm
from main_page.serializers import (
    HeaderSerializer,
    FooterSerializer,
    ContactFormSerializer,
)


class PlotBuildingAPIView(APIView):

    def get(self, request, format=None):
        # Получаем данные для PlotBuilding
        buildings = PlotBuilding.objects.all()
        buildings_serializer = PlotBuildingSerializer(
            buildings, many=True, context={"request": request}
        )

        # Получаем данные для Header, Footer и формы из main_page
        header = Header.objects.first()
        footer = Footer.objects.first()
        contact_form = ContactForm()  # Создаем пустую форму

        header_serializer = HeaderSerializer(header, context={"request": request})
        footer_serializer = FooterSerializer(footer, context={"request": request})
        contact_form_serializer = ContactFormSerializer(contact_form)

        # Формируем объединенный ответ
        response_data = {
            "header": header_serializer.data,
            "main": {
                "content": buildings_serializer.data,
                "contact_form": contact_form_serializer.data,  # Добавляем форму в ответ
            },
            "footer": footer_serializer.data,
        }

        return Response(response_data)

    def post(self, request, format=None):
        # Обработка формы
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Форма успешно отправлена!"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)