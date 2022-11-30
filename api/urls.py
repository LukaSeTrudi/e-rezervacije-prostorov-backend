
from django.urls import path, include
urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('management/', include('api.management.urls')),
]
