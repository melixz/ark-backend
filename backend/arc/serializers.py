from rest_framework import serializers
from .models import (
    City,
    Complex,
    ComplexImage,
    Plot,
    PlotImage,
    Apartment,
    ApartmentImage,
    ApartmentSection,
    PlotLand,
    NewSection,
    PlotSection,
)


class ImageBaseSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        fields = ["image_type", "image_url"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None


class ComplexImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = ComplexImage


class PlotImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = PlotImage


class ApartmentImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = ApartmentImage


class ApartmentSectionSerializer(serializers.ModelSerializer):
    image_1_url = serializers.SerializerMethodField()
    image_2_url = serializers.SerializerMethodField()
    image_3_url = serializers.SerializerMethodField()
    image_4_url = serializers.SerializerMethodField()
    image_5_url = serializers.SerializerMethodField()

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
            "image_1_url",
            "image_2_url",
            "image_3_url",
            "image_4_url",
            "image_5_url",
        ]

    def get_image_1_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_1.url) if obj.image_1 else None

    def get_image_2_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_2.url) if obj.image_2 else None

    def get_image_3_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_3.url) if obj.image_3 else None

    def get_image_4_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_4.url) if obj.image_4 else None

    def get_image_5_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_5.url) if obj.image_5 else None


class ApartmentSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    slider = serializers.SerializerMethodField()
    sections = ApartmentSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ["category", "images", "slider", "sections"]

    def get_images(self, obj):
        request = self.context.get("request")
        additional_images = obj.images.filter(image_type="additional_image")
        return [
            request.build_absolute_uri(image.image.url) if image.image else None
            for image in additional_images
        ]

    def get_slider(self, obj):
        request = self.context.get("request")
        slider_images = obj.images.filter(image_type="slider_image")
        return [
            request.build_absolute_uri(image.image.url) if image.image else None
            for image in slider_images
        ]


class ComplexSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)
    images = ComplexImageSerializer(many=True, read_only=True)
    card_bg = serializers.SerializerMethodField()

    class Meta:
        model = Complex
        fields = [
            "name",
            "path",
            "card_bg",
            "apartments",
            "images",
        ]

    def get_card_bg(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.card_bg.url) if obj.card_bg else None


class PlotLandSerializer(serializers.ModelSerializer):
    land_type_display = serializers.CharField(
        source="get_land_type_display", read_only=True
    )

    class Meta:
        model = PlotLand
        fields = ["land_type", "land_type_display", "price"]


class PlotSerializer(serializers.ModelSerializer):
    lands = PlotLandSerializer(many=True, read_only=True)
    images = PlotImageSerializer(many=True, read_only=True)
    card_bg = serializers.SerializerMethodField()

    class Meta:
        model = Plot
        fields = ["district", "path", "card_bg", "lands", "images"]

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
        fields = [
            "title",
            "desc_1",
            "desc_2",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "loc",
        ]

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
        fields = [
            "title",
            "desc_1",
            "desc_2",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "loc",
        ]

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
        fields = [
            "name",
            "title",
            "desc",
            "complex_card_bg",
            "complex_bg",
            "path",
            "complexes",
            "section",
        ]

    def get_title(self, obj):
        return obj.new_title

    def get_desc(self, obj):
        return obj.new_desc

    def get_complex_card_bg(self, obj):
        request = self.context.get("request")
        return (
            request.build_absolute_uri(obj.complex_card_bg.url)
            if obj.complex_card_bg
            else None
        )

    def get_complex_bg(self, obj):
        request = self.context.get("request")
        return (
            request.build_absolute_uri(obj.complex_bg.url) if obj.complex_bg else None
        )


class PlotsCityDataSerializer(serializers.ModelSerializer):
    plots = PlotSerializer(many=True, read_only=True)
    section = PlotSectionSerializer(many=True, source="plot_sections", read_only=True)
    title = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    plot_card_bg = serializers.SerializerMethodField()
    plot_bg = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = [
            "name",
            "title",
            "desc",
            "plot_card_bg",
            "plot_bg",
            "path",
            "plots",
            "section",
        ]

    def get_title(self, obj):
        return obj.plot_title

    def get_desc(self, obj):
        return obj.plot_desc

    def get_plot_card_bg(self, obj):
        request = self.context.get("request")
        return (
            request.build_absolute_uri(obj.plot_card_bg.url)
            if obj.plot_card_bg
            else None
        )

    def get_plot_bg(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.plot_bg.url) if obj.plot_bg else None


class FullResponseSerializer(serializers.Serializer):
    new = NewCityDataSerializer(many=True)
    plots = PlotsCityDataSerializer(many=True)
