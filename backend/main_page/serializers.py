from rest_framework import serializers
from .models import Header, MainContent, SectionOne, SectionTwo, SectionTwoCard, SectionThree, Footer

class HeaderSerializer(serializers.ModelSerializer):
    logo_icon = serializers.SerializerMethodField()
    phone_icon = serializers.SerializerMethodField()
    header_bgr = serializers.SerializerMethodField()
    nav_bgr = serializers.SerializerMethodField()
    bgr_bottom = serializers.SerializerMethodField()

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

    def get_logo_icon(self, obj):
        return self.get_full_url(obj.logo_icon)

    def get_phone_icon(self, obj):
        return self.get_full_url(obj.phone_icon)

    def get_header_bgr(self, obj):
        return self.get_full_url(obj.header_bgr)

    def get_nav_bgr(self, obj):
        return self.get_full_url(obj.nav_bgr)

    def get_bgr_bottom(self, obj):
        return self.get_full_url(obj.bgr_bottom)

    def get_full_url(self, image_field):
        if image_field:
            return self.context['request'].build_absolute_uri(image_field.url)
        return None

class MainContentSerializer(serializers.ModelSerializer):
    bgr_image = serializers.SerializerMethodField()

    class Meta:
        model = MainContent
        fields = ["id", "name", "bgr_image", "path"]

    def get_bgr_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.bgr_image.url)

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
        return self.context['request'].build_absolute_uri(obj.icon.url)

    def get_background(self, obj):
        return self.context['request'].build_absolute_uri(obj.background.url)

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
        return self.context['request'].build_absolute_uri(obj.image.url)

    def get_bgr_button(self, obj):
        return self.context['request'].build_absolute_uri(obj.bgr_button.url)

class FooterSerializer(serializers.ModelSerializer):
    telegram_icon = serializers.SerializerMethodField()
    whatsapp_icon = serializers.SerializerMethodField()
    viber_icon = serializers.SerializerMethodField()
    youtube_icon = serializers.SerializerMethodField()
    vk_icon = serializers.SerializerMethodField()

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

    def get_telegram_icon(self, obj):
        return self.context['request'].build_absolute_uri(obj.telegram_icon.url)

    def get_whatsapp_icon(self, obj):
        return self.context['request'].build_absolute_uri(obj.whatsapp_icon.url)

    def get_viber_icon(self, obj):
        return self.context['request'].build_absolute_uri(obj.viber_icon.url)

    def get_youtube_icon(self, obj):
        return self.context['request'].build_absolute_uri(obj.youtube_icon.url)

    def get_vk_icon(self, obj):
        return self.context['request'].build_absolute_uri(obj.vk_icon.url)
