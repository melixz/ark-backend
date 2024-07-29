from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Header, MainContent, SectionOne, SectionTwo, SectionThree, Footer
from .serializers import (
    HeaderSerializer,
    MainContentSerializer,
    SectionOneSerializer,
    SectionTwoSerializer,
    SectionThreeSerializer,
    FooterSerializer,
)


class PageAPIView(APIView):

    def get(self, request, format=None):
        header = Header.objects.first()
        main_content = MainContent.objects.all()
        section1 = SectionOne.objects.first()
        section2 = SectionTwo.objects.first()
        section3 = SectionThree.objects.first()
        footer = Footer.objects.first()

        header_serializer = HeaderSerializer(header)
        main_content_serializer = MainContentSerializer(main_content, many=True)
        sectionOne_serializer = SectionOneSerializer(section1)
        sectionTwo_serializer = SectionTwoSerializer(section2)
        sectionThree_serializer = SectionThreeSerializer(section3)
        footer_serializer = FooterSerializer(footer)

        return Response(
            {
                "header": header_serializer.data,
                "main": {
                    "content": main_content_serializer.data,
                    "contain": {
                        "section_1": SectionOneSerializer.data,
                        "section_2": SectionTwoSerializer.data,
                        "section_3": SectionThreeSerializer.data,
                    },
                },
                "footer": footer_serializer.data,
            }
        )
