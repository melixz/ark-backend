from rest_framework import serializers
from .models import City, Complex, Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['title', 'desc', 'image_1', 'image_2', 'image_3', 'loc']


class ComplexSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Complex
        fields = ['name', 'path', 'studia', 'one', 'two', 'three', 'sections']


class CitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='name')
    complexes = ComplexSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city', 'image', 'path', 'title', 'desc', 'complexes']
