from rest_framework import serializers
from .models import City, Complex, Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['title', 'desc', 'image_1', 'image_2', 'image_3', 'loc']


class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = ['name', 'path', 'studia', 'one', 'two', 'three']


class CitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='name')
    complexes = ComplexSerializer(many=True, read_only=True)
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city', 'image', 'path', 'title', 'desc', 'complexes', 'sections']
