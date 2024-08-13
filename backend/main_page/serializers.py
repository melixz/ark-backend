from rest_framework import serializers
from .models import Header, MainContent, Advantages, Card, ContactForm, Footer


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ["phone_number", "header_title", "header_title_bottom"]


class MainContentSerializer(serializers.ModelSerializer):
    bgr_image = serializers.SerializerMethodField()
    routes = serializers.SerializerMethodField()

    class Meta:
        model = MainContent
        fields = ["name", "bgr_image", "path", "class_name", "routes"]

    def get_bgr_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.bgr_image.url) if obj.bgr_image else None

    def get_routes(self, obj):
        return obj.routes


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = [
            "title",
            "desc",
            "climate",
            "nature",
            "accessibility",
            "infrastructure",
            "possibilities",
        ]


class CardSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ["title", "description", "path", "image"]

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "phone", "message", "consent"]


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ["phone_number", "color_text"]
