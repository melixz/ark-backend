from rest_framework import serializers
from .base import SectionImageMixin, build_path
from ..models.city import City, NewSection
from ..models.plot import PlotSection
from .complex import ComplexSerializer
from .plot import PlotSerializer


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


class NewCityDataSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    complexes = ComplexSerializer(many=True, read_only=True)
    section = NewSectionSerializer(many=True, source="new_sections", read_only=True)
    complex_card_bg = serializers.ImageField(read_only=True)
    complex_bg = serializers.ImageField(read_only=True)

    class Meta:
        model = City
        fields = [
            "name",
            "new_title",
            "new_desc",
            "complex_card_bg",
            "complex_bg",
            "path",
            "complexes",
            "section",
        ]

    def get_path(self, obj):
        return build_path(obj.path)


class PlotsCityDataSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    plots = PlotSerializer(many=True, read_only=True)
    section = PlotSectionSerializer(many=True, source="plot_sections", read_only=True)
    plot_card_bg = serializers.ImageField(read_only=True)
    plot_bg = serializers.ImageField(read_only=True)

    class Meta:
        model = City
        fields = [
            "name",
            "plot_title",
            "plot_desc",
            "plot_card_bg",
            "plot_bg",
            "path",
            "plots",
            "section",
        ]

    def get_path(self, obj):
        return build_path(obj.path)
