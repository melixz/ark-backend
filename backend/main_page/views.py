from rest_framework import viewsets
from .models import Header, MainSection, FooterSection
from .serializers import HeaderSerializer, MainSectionSerializer, FooterSectionSerializer


class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class MainSectionViewSet(viewsets.ModelViewSet):
    queryset = MainSection.objects.all()
    serializer_class = MainSectionSerializer


class FooterSectionViewSet(viewsets.ModelViewSet):
    queryset = FooterSection.objects.all()
    serializer_class = FooterSectionSerializer
