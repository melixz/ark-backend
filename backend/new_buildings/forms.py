from django import forms
from .models import NewBuilding


class NewBuildingForm(forms.ModelForm):
    class Meta:
        model = NewBuilding
        fields = ["name", "bgr_image", "path", "class_name"]
        widgets = {
            "path": forms.TextInput(attrs={"size": 40}),
        }
