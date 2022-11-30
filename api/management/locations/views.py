
from api.management.locations.serializers import LocationDetailSerializer, LocationCreateSerializer, LocationListSerializer
from api.mixins import MultipleSerializersMixin
from apps.locations.models import Location

from rest_framework import viewsets


class LocationViewSet(MultipleSerializersMixin, viewsets.ModelViewSet):
    serializers = {
        'default': LocationDetailSerializer,
        'retrieve': LocationDetailSerializer,
        'create': LocationCreateSerializer,
        'update': LocationCreateSerializer,
        'list': LocationListSerializer
    }

    def get_queryset(self):
        return Location.objects.filter(owner=self.request.user)

