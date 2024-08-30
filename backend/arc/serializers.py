from rest_framework import serializers
from .models import City, Complex, Plot, Section, Apartment, ApartmentImage


class ApartmentImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ApartmentImage
        fields = ["image_type", "image_url"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None


class ApartmentSerializer(serializers.ModelSerializer):
    images = ApartmentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ["category", "images"]


class ComplexSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Complex
        fields = ["name", "path", "studia", "one", "two", "three", "apartments"]


class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ["district", "path"]


class SectionSerializer(serializers.ModelSerializer):
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ["title", "desc", "image_1", "image_2", "image_3", "loc"]

    def get_image_1(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_1.url) if obj.image_1 else None

    def get_image_2(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_2.url) if obj.image_2 else None

    def get_image_3(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_3.url) if obj.image_3 else None


class NewCityDataSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    complexes = ComplexSerializer(many=True, read_only=True)
    section_1 = SectionSerializer(many=True, source="sections", read_only=True)
    section_2 = SectionSerializer(many=True, source="sections", read_only=True)

    title = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = [
            "name",
            "title",
            "desc",
            "image",
            "path",
            "complexes",
            "section_1",
            "section_2",
        ]

    def get_title(self, obj):
        return obj.new_title

    def get_desc(self, obj):
        return obj.new_desc

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None


class PlotsCityDataSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    plots = PlotSerializer(many=True, read_only=True)

    title = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ["name", "title", "desc", "image", "path", "plots"]

    def get_title(self, obj):
        return obj.plot_title

    def get_desc(self, obj):
        return obj.plot_desc

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None


class FullResponseSerializer(serializers.Serializer):
    new = NewCityDataSerializer(many=True)
    plots = PlotsCityDataSerializer(many=True)
