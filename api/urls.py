
from django.urls import path, include
from api.schedules.views import CourtScheduleAPIView
from api.users.views import UserViewSet
from api.views import CourtTypeAPIView


from rest_framework.routers import DefaultRouter
from api.locations.views import LocationCourtViewSet, LocationViewSet
router = DefaultRouter()

router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'courts', LocationCourtViewSet, basename='courts')
router.register(r'users', UserViewSet, basename='users')

#router.register(r'schedules', CourtScheduleViewSet, basename='schedules')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('api.auth.urls')),
    path('management/', include('api.management.urls')),
    path('court-types/', CourtTypeAPIView.as_view(), name='court-types'),
    path('schedules/', CourtScheduleAPIView.as_view(), name='schedules'),
]
