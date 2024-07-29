from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Header, MainContent, Section1, Section2, Section3, Footer
from .serializers import (
    HeaderSerializer,
    MainContentSerializer,
    Section1Serializer,
    Section2Serializer,
    Section3Serializer,
    FooterSerializer,
)


class PageAPIView(APIView):

    def get(self, request, format=None):
        header = Header.objects.first()
        main_content = MainContent.objects.all()
        section1 = Section1.objects.first()
        section2 = Section2.objects.first()
        section3 = Section3.objects.first()
        footer = Footer.objects.first()

        header_serializer = HeaderSerializer(header)
        main_content_serializer = MainContentSerializer(main_content, many=True)
        section1_serializer = Section1Serializer(section1)
        section2_serializer = Section2Serializer(section2)
        section3_serializer = Section3Serializer(section3)
        footer_serializer = FooterSerializer(footer)

        return Response(
            {
                "header": header_serializer.data,
                "main": {
                    "content": main_content_serializer.data,
                    "contain": {
                        "section_1": section1_serializer.data,
                        "section_2": section2_serializer.data,
                        "section_3": section3_serializer.data,
                    },
                },
                "footer": footer_serializer.data,
            }
        )
