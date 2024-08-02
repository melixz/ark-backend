from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding
from .serializers import NewBuildingSerializer


class NewBuildingsAPIView(APIView):

    def get(self, request, format=None):
        buildings = NewBuilding.objects.all()
        serializer = NewBuildingSerializer(
            buildings, many=True, context={"request": request}
        )
        return Response(
            {
                # "header": {
                #     "phone_number": "",
                #     "header_title": "",
                #     "header_title_bottom": ""
                # },
                "main": {
                    "content": serializer.data,
                    "contain": {
                        "section_1": {
                            "title": "Работает",
                            "desc": "",
                            "climate": "",
                            "nature": "",
                            "accessibility": "",
                            "infrastructure": "",
                            "possibilities": "",
                        },
                        "section_2": {"title": ""},
                        "section_3": {
                            "tg_link": "",
                            "viber_link": "",
                            "whatsup_link": "",
                        },
                    },
                },
                # "footer": {
                #     "phone_number": "",
                #     "color_text": ""
                # }
            }
        )
