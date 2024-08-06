from django import forms
from .models import MainContent, Card


class MainContentForm(forms.ModelForm):
    class Meta:
        model = MainContent
        fields = ["name", "bgr_image", "path", "class_name"]
        widgets = {
            "path": forms.TextInput(attrs={"size": 40}),
        }


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["title", "description", "path", "image"]
        widgets = {
            "path": forms.TextInput(attrs={"size": 40}),
        }
