from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Header, MainSection
from .serializers import HeaderSerializer, MainSectionSerializer


class PageAPIView(APIView):

    def get(self, request, format=None):
        header = Header.objects.first()
        main_sections = MainSection.objects.all()

        header_serializer = HeaderSerializer(header)
        main_sections_serializer = MainSectionSerializer(main_sections, many=True)

        return Response({
            "header": header_serializer.data,
            "main": {"sections": main_sections_serializer.data},
        })
