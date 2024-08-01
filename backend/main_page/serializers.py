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
        fields = ["phone_number", "header_title", "header_title_bottom"]


class MainContentSerializer(serializers.ModelSerializer):
    bgr_image = serializers.SerializerMethodField()

    class Meta:
        model = MainContent
        fields = ["name", "bgr_image", "path", "class_name"]

    def get_bgr_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.bgr_image.url)


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
    icon = serializers.SerializerMethodField()
    background = serializers.SerializerMethodField()

    class Meta:
        model = SectionTwoCard
        fields = ["icon", "title", "description", "background", "button_text"]

    def get_icon(self, obj):
        return self.context["request"].build_absolute_uri(obj.icon.url)

    def get_background(self, obj):
        return self.context["request"].build_absolute_uri(obj.background.url)


class SectionTwoSerializer(serializers.ModelSerializer):
    cards = SectionTwoCardSerializer(many=True, read_only=True)

    class Meta:
        model = SectionTwo
        fields = ["title", "cards"]


class SectionThreeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    bgr_button = serializers.SerializerMethodField()

    class Meta:
        model = SectionThree
        fields = ["image", "tg_link", "viber_link", "whatsup_link", "bgr_button"]

    def get_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.image.url)

    def get_bgr_button(self, obj):
        return self.context["request"].build_absolute_uri(obj.bgr_button.url)


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ["phone_number", "color_text"]
