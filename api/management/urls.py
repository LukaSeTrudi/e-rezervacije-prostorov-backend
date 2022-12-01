from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api.management.locations.views import LocationViewSet, LocationCourtViewSet
router = DefaultRouter()

router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'locations/(?P<location_pk>[0-9]+)/courts', LocationCourtViewSet, basename='courts')

urlpatterns = [
    path('', include(router.urls)),
]
