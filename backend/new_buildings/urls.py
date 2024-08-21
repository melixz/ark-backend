from django.urls import path, include
from .views import NewBuildingsAPIView

urlpatterns = [
    path("page/new/", NewBuildingsAPIView.as_view(), name="new_buildings"),
    path("page/new/developers/", include("developers.urls")),  # Вложенный маршрут для developers
]
