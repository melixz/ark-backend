from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding
from .serializers import NewBuildingSerializer
from main_page.models import Header, Footer
from main_page.serializers import HeaderSerializer, FooterSerializer


class NewBuildingsAPIView(APIView):

    def get(self, request, format=None):
        # Получаем данные для NewBuilding
        buildings = NewBuilding.objects.all()
        buildings_serializer = NewBuildingSerializer(
            buildings, many=True, context={"request": request}
        )

        # Получаем данные для Header и Footer из main_page
        header = Header.objects.first()
        footer = Footer.objects.first()
        header_serializer = HeaderSerializer(header, context={"request": request})
        footer_serializer = FooterSerializer(footer, context={"request": request})

        # Формируем объединенный ответ
        response_data = {
            "header": header_serializer.data,
            "main": {
                "content": buildings_serializer.data,
                "contain": {
                    "section_1": {
                        "title": "",
                        "desc": "",
                        "climate": "",
                        "nature": "",
                        "accessibility": "",
                        "infrastructure": "",
                        "possibilities": "",
                    },
                    "section_2": {"title": ""},
                    "section_3": {"tg_link": "", "viber_link": "", "whatsup_link": ""},
                },
            },
            "footer": footer_serializer.data,
        }

        return Response(response_data)
