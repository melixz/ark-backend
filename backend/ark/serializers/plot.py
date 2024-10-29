from rest_framework import serializers
from .base import ImageBaseSerializer
from ..models.plot import Plot, PlotImage


class PlotImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = PlotImage


class PlotSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    slider = serializers.SerializerMethodField()
    lands = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    card_bg = serializers.ImageField(read_only=True)

    class Meta:
        model = Plot
        fields = [
            "district",
            "path",
            "title",
            "desk",
            "card_bg",
            "images",
            "slider",
            "lands",
        ]

    def get_path(self, obj):
        return obj.path.split("/")[-1]

    def get_images_by_type(self, obj, image_type):
        images = obj.images.filter(image_type=image_type)
        serializer = PlotImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_images(self, obj):
        return self.get_images_by_type(obj, "additional_image")

    def get_slider(self, obj):
        return self.get_images_by_type(obj, "slider_image")
