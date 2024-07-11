from rest_framework import serializers
from .models import Header, MainSection, FooterSection


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class MainSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSection
        fields = '__all__'


class FooterSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSection
        fields = '__all__'
