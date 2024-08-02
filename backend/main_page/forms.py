from django import forms
from .models import MainContent


class MainContentForm(forms.ModelForm):
    class Meta:
        model = MainContent
        fields = ["name", "bgr_image", "path", "class_name"]
        widgets = {
            "path": forms.TextInput(attrs={"size": 40}),
        }
