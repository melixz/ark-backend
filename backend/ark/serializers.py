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
    PlotLandImage,
    PlotLandSection,
    DynamicFormSubmission,
)


# Базовый сериализатор для ImageBase моделей
class ImageBaseSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source="image", read_only=True)

    class Meta:
        fields = ["image_type", "image_url"]


# Сериализаторы для моделей изображений
class ComplexImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = ComplexImage


class PlotImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = PlotImage


class ApartmentImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = ApartmentImage


class PlotLandImageSerializer(ImageBaseSerializer):
    class Meta(ImageBaseSerializer.Meta):
        model = PlotLandImage


# Базовый миксин для секций с изображениями
class SectionImageMixin(serializers.ModelSerializer):
    image_fields = []

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.extend(self.image_fields)
        return fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request")
        for image_field in self.image_fields:
            image = getattr(instance, image_field, None)
            if image:
                representation[image_field] = request.build_absolute_uri(image.url)
            else:
                representation[image_field] = None
        return representation


# Сериализатор для ApartmentSection
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


# Сериализатор для PlotLandSection
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


# Сериализатор для Apartment
class ApartmentSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
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
            "floor_count",
        ]

    def get_path(self, obj):
        city_path = (
            obj.complex.city.path.strip("/")
            if obj.complex and obj.complex.city and obj.complex.city.path
            else ""
        )
        complex_path = (
            obj.complex.path.strip("/") if obj.complex and obj.complex.path else ""
        )
        apartment_path = obj.path.strip("/") if obj.path else ""
        return f"/new/{city_path}/{complex_path}/{apartment_path}"

    def get_images_by_type(self, obj, image_type):
        images = obj.images.filter(image_type=image_type)
        serializer = ApartmentImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_images(self, obj):
        return self.get_images_by_type(obj, "additional_image")

    def get_slider(self, obj):
        return self.get_images_by_type(obj, "slider_image")


# Сериализатор для Complex
class ComplexSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    desk = serializers.CharField(read_only=True)
    images = serializers.SerializerMethodField()
    slider = serializers.SerializerMethodField()
    apartments = ApartmentSerializer(many=True, read_only=True)
    card_bg = serializers.ImageField(read_only=True)

    class Meta:
        model = Complex
        fields = [
            "name",
            "path",
            "desk",
            "card_bg",
            "images",
            "slider",
            "apartments",
        ]

    def get_path(self, obj):
        city_path = obj.city.path.strip("/") if obj.city and obj.city.path else ""
        complex_path = obj.path.strip("/") if obj.path else ""
        return f"/new/{city_path}/{complex_path}"

    def get_images_by_type(self, obj, image_type):
        images = obj.images.filter(image_type=image_type)
        serializer = ComplexImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_images(self, obj):
        return self.get_images_by_type(obj, "additional_image")

    def get_slider(self, obj):
        return self.get_images_by_type(obj, "slider_image")


# Сериализатор для PlotLand
class PlotLandSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
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
            "images",
            "slider",
            "sections",
        ]

    def get_path(self, obj):
        plot_path = obj.plot.path.strip("/") if obj.plot and obj.plot.path else ""
        land_path = obj.path.strip("/") if obj.path else ""
        return f"/{plot_path}/{land_path}"

    def get_images_by_type(self, obj, image_type):
        images = obj.images.filter(image_type=image_type)
        serializer = PlotLandImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_images(self, obj):
        return self.get_images_by_type(obj, "additional_image")

    def get_slider(self, obj):
        return self.get_images_by_type(obj, "slider_image")


# Сериализатор для Plot
class PlotSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    desk = serializers.CharField()
    images = serializers.SerializerMethodField()
    slider = serializers.SerializerMethodField()
    lands = PlotLandSerializer(many=True, read_only=True)
    card_bg = serializers.ImageField(read_only=True)

    class Meta:
        model = Plot
        fields = [
            "district",
            "path",
            "desk",
            "card_bg",
            "images",
            "slider",
            "lands",
        ]

    def get_path(self, obj):
        city_path = obj.city.path.strip("/") if obj.city and obj.city.path else ""
        plot_path = obj.path.strip("/") if obj.path else ""
        return f"/plots/{city_path}/{plot_path}"

    def get_images_by_type(self, obj, image_type):
        images = obj.images.filter(image_type=image_type)
        serializer = PlotImageSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_images(self, obj):
        return self.get_images_by_type(obj, "additional_image")

    def get_slider(self, obj):
        return self.get_images_by_type(obj, "slider_image")


# Сериализатор для NewSection
class NewSectionSerializer(SectionImageMixin, serializers.ModelSerializer):
    image_fields = ["image_1", "image_2", "image_3", "image_4"]

    class Meta:
        model = NewSection
        fields = [
            "title",
            "desc_1",
            "desc_2",
            "loc",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
        ]


# Сериализатор для PlotSection
class PlotSectionSerializer(SectionImageMixin, serializers.ModelSerializer):
    image_fields = ["image_1", "image_2", "image_3", "image_4"]

    class Meta:
        model = PlotSection
        fields = [
            "title",
            "desc_1",
            "desc_2",
            "loc",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
        ]


# Сериализатор для City (новостройки)
class NewCityDataSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    complexes = ComplexSerializer(many=True, read_only=True)
    section = NewSectionSerializer(many=True, source="new_sections", read_only=True)
    title = serializers.CharField(source="new_title", read_only=True)
    desc = serializers.CharField(source="new_desc", read_only=True)
    complex_card_bg = serializers.ImageField(read_only=True)
    complex_bg = serializers.ImageField(read_only=True)

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

    def get_path(self, obj):
        city_path = obj.path.strip("/") if obj.path else ""
        return f"/new/{city_path}"


# Сериализатор для City (застройки)
class PlotsCityDataSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    plots = PlotSerializer(many=True, read_only=True)
    section = PlotSectionSerializer(many=True, source="plot_sections", read_only=True)
    title = serializers.CharField(source="plot_title", read_only=True)
    desc = serializers.CharField(source="plot_desc", read_only=True)
    plot_card_bg = serializers.ImageField(read_only=True)
    plot_bg = serializers.ImageField(read_only=True)

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

    def get_path(self, obj):
        city_path = obj.path.strip("/") if obj.path else ""
        return f"/plots/{city_path}"


# Сериализатор для отправок динамических форм
class DynamicFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicFormSubmission
        fields = ["name", "data", "submitted_at"]
        read_only_fields = ["submitted_at"]


# Сериализатор для полного ответа
class FullResponseSerializer(serializers.Serializer):
    new = NewCityDataSerializer(many=True)
    plots = PlotsCityDataSerializer(many=True)
