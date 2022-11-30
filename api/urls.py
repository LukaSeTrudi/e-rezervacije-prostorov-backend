
from django.urls import path, include


from rest_framework.routers import DefaultRouter
from api.locations.views import LocationViewSet
router = DefaultRouter()

router.register(r'locations', LocationViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('api.auth.urls')),
    path('management/', include('api.management.urls')),
]
