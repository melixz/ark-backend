from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Header, MainContent, Advantages, Card, Footer, ContactForm
from .serializers import (
    HeaderSerializer,
    MainContentSerializer,
    AdvantagesSerializer,
    CardSerializer,
    FooterSerializer,
    ContactFormSerializer,
)


class PageAPIView(APIView):
    def get(self, request, format=None):
        header = Header.objects.first()
        main_content = MainContent.objects.all()
        advantages = Advantages.objects.first()
        cards = Card.objects.all()
        footer = Footer.objects.first()

        header_serializer = HeaderSerializer(header, context={"request": request})
        main_content_serializer = MainContentSerializer(
            main_content, many=True, context={"request": request}
        )
        advantages_serializer = AdvantagesSerializer(
            advantages, context={"request": request}
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
                        "advantages": advantages_serializer.data,
                        "cards": cards_serializer.data,
                    },
                },
                "footer": footer_serializer.data,
            }
        )

    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Форма успешно отправлена!"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
