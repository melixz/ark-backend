from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Developer
from .serializers import DeveloperSerializer
from main_page.models import Header, Footer, ContactForm
from main_page.serializers import (
    HeaderSerializer,
    FooterSerializer,
    ContactFormSerializer,
)


class DeveloperAPIView(APIView):

    def get(self, request, format=None):
        developers = Developer.objects.all()
        developers_serializer = DeveloperSerializer(
            developers, many=True, context={"request": request}
        )

        header = Header.objects.first()
        footer = Footer.objects.first()
        contact_form = ContactForm()

        header_serializer = HeaderSerializer(header, context={"request": request})
        footer_serializer = FooterSerializer(footer, context={"request": request})
        contact_form_serializer = ContactFormSerializer(contact_form)

        response_data = {
            "header": header_serializer.data,
            "main": {
                "content": developers_serializer.data,
                "contact_form": contact_form_serializer.data,
            },
            "footer": footer_serializer.data,
        }

        return Response(response_data)

    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Форма успешно отправлена!"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
