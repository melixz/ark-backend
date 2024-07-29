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

        header_serializer = HeaderSerializer(header, context={'request': request})
        main_content_serializer = MainContentSerializer(main_content, many=True, context={'request': request})
        section_one_serializer = SectionOneSerializer(section1, context={'request': request})
        section_two_serializer = SectionTwoSerializer(section2, context={'request': request})
        section_three_serializer = SectionThreeSerializer(section3, context={'request': request})
        footer_serializer = FooterSerializer(footer, context={'request': request})

        return Response(
            {
                "header": header_serializer.data,
                "main": {
                    "content": main_content_serializer.data,
                    "contain": {
                        "section_1": section_one_serializer.data,
                        "section_2": section_two_serializer.data,
                        "section_3": section_three_serializer.data,
                    },
                },
                "footer": footer_serializer.data,
            }
        )
