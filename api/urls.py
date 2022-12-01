
from django.urls import path, include
from api.users.views import UserViewSet
from api.views import CourtTypeAPIView


from rest_framework.routers import DefaultRouter
from api.locations.views import LocationViewSet
router = DefaultRouter()

router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('api.auth.urls')),
    path('management/', include('api.management.urls')),
    path('court-types/', CourtTypeAPIView.as_view(), name='court-types'),
]
