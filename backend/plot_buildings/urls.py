from django.urls import path
from .views import PlotBuildingAPIView

urlpatterns = [
    path("page/plots/", PlotBuildingAPIView.as_view(), name="plots-api"),
]
