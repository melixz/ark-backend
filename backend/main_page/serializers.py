from rest_framework import serializers
from .models import Header, MainSection, Footer


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = [
            "logo",
            "navigation_background_color",
            "phone_icon",
            "phone_number",
            "header_background",
            "title",
            "description",
        ]


class MainSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSection
        fields = ["title", "content", "image", "url"]


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ["telegram_icon", "whatsapp_icon", "viber_icon", "vk_icon"]
