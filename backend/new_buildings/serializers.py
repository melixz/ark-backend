from rest_framework import serializers
from .models import NewBuilding
from main_page.serializers import ContactFormSerializer
from main_page.models import ContactForm


class NewBuildingSerializer(serializers.ModelSerializer):
    bgr_image = serializers.SerializerMethodField()
    routes = serializers.SerializerMethodField()

    class Meta:
        model = NewBuilding
        fields = ["name", "bgr_image", "path", "class_name", "routes"]

    def get_bgr_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.bgr_image.url)

    def get_routes(self, obj):
        return obj.routes

    def get_contact_form(self, obj):
        # Создаем или получаем экземпляр ContactForm (например, можно создать новый)
        contact_form = (
            ContactForm()
        )  # Или можно получить существующую форму, если она одна
        return ContactFormSerializer(contact_form).data
