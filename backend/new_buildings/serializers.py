from rest_framework import serializers
from .models import NewBuilding


class NewBuildingSerializer(serializers.ModelSerializer):
    bgr_image = serializers.SerializerMethodField()
    routes = serializers.SerializerMethodField()

    class Meta:
        model = NewBuilding
        fields = ["name", "bgr_image", "path", "class_name", "routes"]

    def get_bgr_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.bgr_image.url)

    def get_routes(self, obj):
        return obj.routes
