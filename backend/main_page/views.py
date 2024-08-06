from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Header, MainContent, SectionOne, Card, Footer
from .serializers import (
    HeaderSerializer,
    MainContentSerializer,
    SectionOneSerializer,
    CardSerializer,
    FooterSerializer,
)


class PageAPIView(APIView):
    def get(self, request, format=None):
        header = Header.objects.first()
        main_content = MainContent.objects.all()
        section1 = SectionOne.objects.first()
        cards = Card.objects.all()
        footer = Footer.objects.first()

        header_serializer = HeaderSerializer(header, context={"request": request})
        main_content_serializer = MainContentSerializer(
            main_content, many=True, context={"request": request}
        )
        section_one_serializer = SectionOneSerializer(
            section1, context={"request": request}
        )
        cards_serializer = CardSerializer(
            cards, many=True, context={"request": request}
        )
        footer_serializer = FooterSerializer(footer, context={"request": request})

        return Response(
            {
                "header": header_serializer.data,
                "main": {
                    "content": main_content_serializer.data,
                    "contain": {
                        "section_1": section_one_serializer.data,
                        "cards": cards_serializer.data,
                    },
                },
                "footer": footer_serializer.data,
            }
        )
