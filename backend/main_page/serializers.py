from rest_framework import serializers
from .models import Header, MainSection, FooterSection


class HeaderSerializer(serializers.ModelSerializer):
    left = serializers.SerializerMethodField()
    center = serializers.SerializerMethodField()
    right = serializers.SerializerMethodField()

    class Meta:
        model = Header
        fields = ['left', 'center', 'right']

    def get_left(self, obj):
        return {
            "type": "image",
            "src": obj.left_image.url,
            "alt": obj.left_alt
        }

    def get_center(self, obj):
        return {
            "type": "banner",
            "text": obj.center_text
        }

    def get_right(self, obj):
        return {
            "buttons": obj.right_buttons
        }


class MainSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSection
        fields = ['title', 'content']


class FooterSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSection
        fields = ['title', 'content']
