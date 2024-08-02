from django.urls import path
from .views import NewBuildingsAPIView

urlpatterns = [
    path('page/new/', NewBuildingsAPIView.as_view(), name='new_buildings'),
]

