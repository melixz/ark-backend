from django.urls import path
from .views import DeveloperAPIView

urlpatterns = [
    path("", DeveloperAPIView.as_view(), name="developers"),
]
