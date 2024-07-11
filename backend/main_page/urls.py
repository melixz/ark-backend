from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeaderViewSet, MainSectionViewSet, FooterSectionViewSet

router = DefaultRouter()
router.register(r'headers', HeaderViewSet)
router.register(r'main-sections', MainSectionViewSet)
router.register(r'footer-sections', FooterSectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
