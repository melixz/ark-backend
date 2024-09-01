from rest_framework import serializers
from .models import City, Complex, Plot, Apartment, ApartmentImage, PlotLand, NewSection, PlotSection


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
    card_bg = serializers.SerializerMethodField()

    class Meta:
        model = Complex
        fields = ["name", "path", "card_bg", "studia", "one", "two", "three", "apartments"]

    def get_card_bg(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.card_bg.url) if obj.card_bg else None


class PlotLandSerializer(serializers.ModelSerializer):
    land_type_display = serializers.CharField(source="get_land_type_display", read_only=True)

    class Meta:
        model = PlotLand
        fields = ["land_type", "land_type_display", "price"]


class PlotSerializer(serializers.ModelSerializer):
    card_bg = serializers.SerializerMethodField()
    lands = PlotLandSerializer(many=True, read_only=True)

    class Meta:
        model = Plot
        fields = ["district", "path", "card_bg", "lands"]

    def get_card_bg(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.card_bg.url) if obj.card_bg else None


class NewSectionSerializer(serializers.ModelSerializer):
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()
    image_4 = serializers.SerializerMethodField()

    class Meta:
        model = NewSection
        fields = ["title", "desc_1", "desc_2", "image_1", "image_2", "image_3", "image_4", "loc"]

    def get_image_1(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_1.url) if obj.image_1 else None

    def get_image_2(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_2.url) if obj.image_2 else None

    def get_image_3(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_3.url) if obj.image_3 else None

    def get_image_4(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_4.url) if obj.image_4 else None


class PlotSectionSerializer(serializers.ModelSerializer):
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()
    image_4 = serializers.SerializerMethodField()

    class Meta:
        model = PlotSection
        fields = ["title", "desc_1", "desc_2", "image_1", "image_2", "image_3", "image_4", "loc"]

    def get_image_1(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_1.url) if obj.image_1 else None

    def get_image_2(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_2.url) if obj.image_2 else None

    def get_image_3(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_3.url) if obj.image_3 else None

    def get_image_4(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_4.url) if obj.image_4 else None


class NewCityDataSerializer(serializers.ModelSerializer):
    complexes = ComplexSerializer(many=True, read_only=True)
    section = NewSectionSerializer(many=True, source="new_sections", read_only=True)
    title = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    complex_card_bg = serializers.SerializerMethodField()
    complex_bg = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ["name", "title", "desc", "complex_card_bg", "complex_bg", "path", "complexes", "section"]

    def get_title(self, obj):
        return obj.new_title

    def get_desc(self, obj):
        return obj.new_desc

    def get_complex_card_bg(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.complex_card_bg.url) if obj.complex_card_bg else None

    def get_complex_bg(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.complex_bg.url) if obj.complex_bg else None


class PlotsCityDataSerializer(serializers.ModelSerializer):
    plots = PlotSerializer(many=True, read_only=True)
    section = PlotSectionSerializer(many=True, source="plot_sections", read_only=True)
    title = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    plot_card_bg = serializers.SerializerMethodField()
    plot_bg = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ["name", "title", "desc", "plot_card_bg", "plot_bg", "path", "plots", "section"]

    def get_title(self, obj):
        return obj.plot_title

    def get_desc(self, obj):
        return obj.plot_desc

    def get_plot_card_bg(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.plot_card_bg.url) if obj.plot_card_bg else None

    def get_plot_bg(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.plot_bg.url) if obj.plot_bg else None


class FullResponseSerializer(serializers.Serializer):
    new = NewCityDataSerializer(many=True)
    plots = PlotsCityDataSerializer(many=True)
