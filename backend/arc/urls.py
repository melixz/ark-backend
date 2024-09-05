from django.urls import path
from .views import FullDataAPIView, DynamicFormSubmissionView

urlpatterns = [
    path("full-data/", FullDataAPIView.as_view(), name="full-data"),
    path(
        "submit-form/", DynamicFormSubmissionView.as_view(), name="submit-form"
    ),  # Этот путь должен существовать
]
