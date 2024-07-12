from rest_framework import serializers
from .models import Header, MainSection, FooterSection


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = [
            'logo', 'navigation_background_color', 'telegram_icon',
            'whatsapp_icon', 'viber_icon', 'phone_icon', 'header_background',
            'title', 'description'
        ]


class MainSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSection
        fields = ['title', 'content']


class FooterSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSection
        fields = ['title', 'content']
