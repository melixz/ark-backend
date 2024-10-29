from rest_framework import serializers


def build_path(*segments):
    """
    Объединяет сегменты пути, гарантируя отсутствие лишних слешей и ведущего слэша.
    """
    return "/".join(segment.strip("/") for segment in segments if segment)


class ImageBaseSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        fields = ["image_type", "image_url"]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            return request.build_absolute_uri(obj.image.url)
        return None


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
