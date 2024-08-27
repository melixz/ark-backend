from django.urls import path
from .views import FullDataAPIView

urlpatterns = [
    path('full-data/', FullDataAPIView.as_view(), name='full-data'),
]
