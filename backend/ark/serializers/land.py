from rest_framework import serializers
from .base import ImageBaseSerializer, SectionImageMixin
from ..models.land import PlotLand, PlotLandImage, PlotLandSection


class PlotLandImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = PlotLandImage


class PlotLandSectionSerializer(SectionImageMixin, serializers.ModelSerializer):
    image_fields = ["image_1", "image_2", "image_3", "image_4", "image_5"]

    class Meta:
        model = PlotLandSection
        fields = [
            "title",
            "price",
            "area",
            "land_status",
            "gas",
            "electricity",
            "water",
            "sewage",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]


class PlotLandSerializer(serializers.ModelSerializer):
    land_type_display = serializers.CharField(
        source="get_land_type_display", read_only=True
    )
    images = serializers.SerializerMethodField()
    slider = serializers.SerializerMethodField()
    sections = PlotLandSectionSerializer(many=True, read_only=True)

    class Meta:
        model = PlotLand
        fields = [
            "land_type",
            "path",
            "land_type_display",
            "area",
            "price",
            "gas",
            "electricity",
            "water",
            "sewage",
            "developed",
            "title",
            "desk",
            "images",
            "slider",
            "sections",
        ]

    def get_images_by_type(self, obj, image_type):
        images = obj.images.filter(image_type=image_type)
        serializer = PlotLandImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_images(self, obj):
        return self.get_images_by_type(obj, "additional_image")

    def get_slider(self, obj):
        return self.get_images_by_type(obj, "slider_image")
