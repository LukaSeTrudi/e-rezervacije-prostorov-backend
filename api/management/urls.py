from django.contrib import admin
from django.urls import path, include
from api.management.analytics.views import AnalyticsAPIView
from api.management.schedules.views import CourtReservationViewSet, CourtScheduleViewSet

from rest_framework.routers import DefaultRouter
from api.management.locations.views import LocationViewSet, LocationCourtViewSet
router = DefaultRouter()

router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'locations/(?P<location_pk>[0-9]+)/courts', LocationCourtViewSet, basename='courts')
router.register(r'locations/(?P<location_pk>[0-9]+)/courts/(?P<court_pk>[0-9]+)/schedules', CourtScheduleViewSet, basename='schedules')
router.register(r'locations/(?P<location_pk>[0-9]+)/courts/(?P<court_pk>[0-9]+)/schedules/(?P<schedule_pk>[0-9]+)/reservations', CourtReservationViewSet, basename='reservations')
urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', AnalyticsAPIView.as_view(), name='analytics'),
]
