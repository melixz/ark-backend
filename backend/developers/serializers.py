from rest_framework import serializers
from .models import Developer


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = ["title", "description", "path"]
