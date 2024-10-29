from rest_framework import serializers
from .base import ImageBaseSerializer, SectionImageMixin
from ..models.apartment import Apartment, ApartmentImage, ApartmentSection


class ApartmentImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = ApartmentImage


class ApartmentSectionSerializer(SectionImageMixin, serializers.ModelSerializer):
    image_fields = ["image_1", "image_2", "image_3", "image_4", "image_5"]

    class Meta:
        model = ApartmentSection
        fields = [
            "title",
            "price",
            "floor",
            "room_count",
            "apartment_number",
            "area",
            "delivery_date",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]


class ApartmentSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    slider = serializers.SerializerMethodField()
    sections = ApartmentSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = [
            "category",
            "path",
            "images",
            "slider",
            "sections",
            "title",
            "desk",
            "floor_count",
        ]
        read_only_fields = ["path"]

    def get_images_by_type(self, obj, image_type):
        images = obj.images.filter(image_type=image_type)
        serializer = ApartmentImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_images(self, obj):
        return self.get_images_by_type(obj, "additional_image")

    def get_slider(self, obj):
        return self.get_images_by_type(obj, "slider_image")
