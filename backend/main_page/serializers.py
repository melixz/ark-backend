from rest_framework import serializers
from .models import (
    Header,
    MainContent,
    Section1,
    Section2,
    Section2Card,
    Section3,
    Footer,
)


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = [
            "logo_icon",
            "phone_icon",
            "phone_number",
            "header_bgr",
            "header_title",
            "header_title_bottom",
            "nav_bgr",
            "bgr_bottom",
        ]


class MainContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainContent
        fields = ["name", "bgr_image", "url"]


class Section1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section1
        fields = [
            "title",
            "desc",
            "climate",
            "nature",
            "assessability",
            "infrastructure",
            "possibilities",
        ]


class Section2CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section2Card
        fields = ["icon", "title", "description", "background", "button_text"]


class Section2Serializer(serializers.ModelSerializer):
    cards = Section2CardSerializer(many=True, read_only=True)

    class Meta:
        model = Section2
        fields = ["title", "cards"]


class Section3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section3
        fields = ["image", "tg_link", "viber_link", "whatsup_link", "bgr_button"]


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = [
            "telegram_icon",
            "whatsapp_icon",
            "viber_icon",
            "youtube_icon",
            "vk_icon",
            "phone_number",
            "color_text",
        ]
