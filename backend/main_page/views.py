from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Header, MainSection, FooterSection
from .serializers import HeaderSerializer, MainSectionSerializer, FooterSectionSerializer


class PageAPIView(APIView):

    def get(self, request, format=None):
        header = Header.objects.first()
        main_sections = MainSection.objects.all()
        footer_sections = FooterSection.objects.all()

        header_serializer = HeaderSerializer(header)
        main_sections_serializer = MainSectionSerializer(main_sections, many=True)
        footer_sections_serializer = FooterSectionSerializer(footer_sections, many=True)

        return Response({
            "header": header_serializer.data,
            "main": {"sections": main_sections_serializer.data},
            "footer": {"sections": footer_sections_serializer.data}
        })
