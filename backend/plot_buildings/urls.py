from django.urls import path
from .views import PlotAPIView

urlpatterns = [
    path("page/plots/", PlotAPIView.as_view(), name="plots-api"),
]
