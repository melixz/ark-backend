from rest_framework import serializers
from .base import ImageBaseSerializer
from ..models.complex import Complex, ComplexImage
from .apartment import ApartmentSerializer


class ComplexImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = ComplexImage


class ComplexSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    slider = serializers.SerializerMethodField()
    apartments = ApartmentSerializer(many=True, read_only=True)
    card_bg = serializers.ImageField(read_only=True)

    class Meta:
        model = Complex
        fields = [
            "name",
            "path",
            "title",
            "desk",
            "card_bg",
            "images",
            "slider",
            "apartments",
        ]

    def get_path(self, obj):
        return f"/new/{obj.city.path}/{obj.path}"

    def get_images_by_type(self, obj, image_type):
        images = obj.images.filter(image_type=image_type)
        serializer = ComplexImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_images(self, obj):
        return self.get_images_by_type(obj, "additional_image")

    def get_slider(self, obj):
        return self.get_images_by_type(obj, "slider_image")
