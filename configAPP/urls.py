from .views import ActorViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'actor', ActorViewSet)
urlpatterns = [
    path('', include(router.urls))
]