from django import forms
from .models import MainContent, ContactForm, Card


class MainContentForm(forms.ModelForm):
    class Meta:
        model = MainContent
        fields = ["name", "bgr_image", "path", "class_name"]
        widgets = {
            "path": forms.TextInput(attrs={"size": 40}),
        }


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "phone", "message", "consent"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ваше имя, фамилия"}),
            "email": forms.EmailInput(attrs={"placeholder": "Адрес эл. почты"}),
            "phone": forms.TextInput(attrs={"placeholder": "+7 (999) 999-99-99"}),
            "message": forms.Textarea(attrs={"placeholder": "Ваше сообщение"}),
            "consent": forms.CheckboxInput(),
        }


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["title", "description", "path", "image"]
        widgets = {
            "path": forms.TextInput(attrs={"size": 40}),
        }
