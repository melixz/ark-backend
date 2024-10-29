from rest_framework import serializers
from ark.serializers import NewCityDataSerializer, PlotsCityDataSerializer


# Сериализатор для полного ответа
class FullResponseSerializer(serializers.Serializer):
    new = NewCityDataSerializer(many=True)
    plots = PlotsCityDataSerializer(many=True)
