from rest_framework import serializers
from .models import Plot


class PlotSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Plot
        fields = ["name", "image", "location", "area", "price", "description", "path"]

    def get_image(self, obj):
        request = self.context["request"]
        return request.build_absolute_uri(obj.image.url)
