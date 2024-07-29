from rest_framework import serializers
from .models import (
    Header,
    MainContent,
    SectionOne,
    SectionTwo,
    SectionTwoCard,
    SectionThree,
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


class SectionOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionOne
        fields = [
            "title",
            "desc",
            "climate",
            "nature",
            "accessibility",
            "infrastructure",
            "possibilities",
        ]


class SectionTwoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTwoCard
        fields = ["icon", "title", "description", "background", "button_text"]


class SectionTwoSerializer(serializers.ModelSerializer):
    cards = SectionTwoCardSerializer(many=True, read_only=True)

    class Meta:
        model = SectionTwo
        fields = ["title", "cards"]


class SectionThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionThree
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
