from django.urls import path, include
from .views import PlotBuildingAPIView

urlpatterns = [
    path("page/plots/", PlotBuildingAPIView.as_view(), name="plots-api"),
    path("page/plots/developers/", include("developers.urls")),  # Вложенный маршрут для developers
]
