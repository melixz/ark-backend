from rest_framework import serializers
from .models import City, Complex, Plot, Section


class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = ['name', 'path', 'studia', 'one', 'two', 'three']


class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ['name', 'path', 'field_1', 'field_2', 'field_3', 'field_4']


class SectionSerializer(serializers.ModelSerializer):
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ['title', 'desc', 'image_1', 'image_2', 'image_3', 'loc']

    def get_image_1(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image_1.url) if obj.image_1 else None

    def get_image_2(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image_2.url) if obj.image_2 else None

    def get_image_3(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image_3.url) if obj.image_3 else None


class CityDataSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='name')
    image = serializers.SerializerMethodField()
    complexes = ComplexSerializer(many=True, read_only=True)
    plots = PlotSerializer(many=True, read_only=True)
    section_1 = SectionSerializer(many=True, source='sections', read_only=True)
    section_2 = SectionSerializer(many=True, source='sections', read_only=True)

    # Поля title и desc
    title = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ['city', 'title', 'desc', 'image', 'path', 'complexes', 'plots', 'section_1', 'section_2']

    def get_title(self, obj):
        request = self.context.get('request')
        if request.resolver_match.url_name == 'new_endpoint_name':
            return obj.new_title
        elif request.resolver_match.url_name == 'plots_endpoint_name':
            return obj.plot_title
        return None

    def get_desc(self, obj):
        request = self.context.get('request')
        if request.resolver_match.url_name == 'new_endpoint_name':
            return obj.new_desc
        elif request.resolver_match.url_name == 'plots_endpoint_name':
            return obj.plot_desc
        return None


class FullResponseSerializer(serializers.Serializer):
    new = CityDataSerializer(many=True)
    plots = CityDataSerializer(many=True)
