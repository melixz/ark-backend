from django.urls import path, include
from .views import NewBuildingsAPIView

urlpatterns = [
    path("", NewBuildingsAPIView.as_view(), name="new_buildings"),
    path("developers/", include("developers.urls")),  # Вложенный маршрут для developers
]
