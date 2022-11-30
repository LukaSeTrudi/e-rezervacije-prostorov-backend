from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api.management.locations.views import LocationViewSet
router = DefaultRouter()

router.register(r'locations', LocationViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls)),
]
