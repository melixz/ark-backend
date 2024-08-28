from rest_framework import serializers
from .models import City, Complex, Section


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


class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = ['name', 'path', 'studia', 'one', 'two', 'three']


class CitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='name')
    image = serializers.SerializerMethodField()
    complexes = ComplexSerializer(many=True, read_only=True)
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city', 'image', 'path', 'title', 'desc', 'complexes', 'sections']

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if obj.image else None
