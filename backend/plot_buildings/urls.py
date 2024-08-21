from django.urls import path, include
from .views import PlotBuildingAPIView

urlpatterns = [
    path("", PlotBuildingAPIView.as_view(), name="plots-api"),
    path("developers/", include("developers.urls")),  # Вложенный маршрут для developers
]
