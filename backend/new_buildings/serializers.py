from rest_framework import serializers
from .models import NewBuilding
from main_page.serializers import ContactFormSerializer


class NewBuildingSerializer(serializers.ModelSerializer):
    bgr_image = serializers.SerializerMethodField()
    routes = serializers.SerializerMethodField()
    contact_form = ContactFormSerializer()

    class Meta:
        model = NewBuilding
        fields = ["name", "bgr_image", "path", "class_name", "routes", "contact_form"]

    def get_bgr_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.bgr_image.url)

    def get_routes(self, obj):
        return obj.routes
