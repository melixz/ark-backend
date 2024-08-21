from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import NewBuilding
from .serializers import NewBuildingSerializer
from main_page.models import Header, MainContent, Footer, ContactForm
from main_page.serializers import (
    HeaderSerializer,
    MainContentSerializer,
    FooterSerializer,
    ContactFormSerializer,
)


class NewBuildingsAPIView(APIView):

    def get(self, request, format=None):
        # Получаем данные для NewBuilding
        buildings = NewBuilding.objects.all()
        buildings_serializer = NewBuildingSerializer(
            buildings, many=True, context={"request": request}
        )

        # Фильтруем записи MainContent для новостроек
        main_content = MainContent.objects.filter(path__startswith="/new")
        main_content_serializer = MainContentSerializer(
            main_content, many=True, context={"request": request}
        )

        # Получаем данные для Header и Footer
        header = Header.objects.first()
        footer = Footer.objects.first()
        contact_form = ContactForm()  # Создаем пустую форму

        # Сериализация данных
        header_serializer = HeaderSerializer(header, context={"request": request})
        footer_serializer = FooterSerializer(footer, context={"request": request})
        contact_form_serializer = ContactFormSerializer(contact_form)

        # Формируем объединенный ответ
        response_data = {
            "header": header_serializer.data,
            "main": {
                "content": buildings_serializer.data,
                "main_page_content": main_content_serializer.data,  # Добавляем только записи для новостроек
                "contact_form": contact_form_serializer.data,
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
