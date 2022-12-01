
from api.locations.serializers import LocationDetailSerializer, LocationListSerializer
from api.mixins import MultipleSerializersMixin
from apps.locations.models import Location

from rest_framework import viewsets


class LocationViewSet(MultipleSerializersMixin, viewsets.ReadOnlyModelViewSet):
    serializers = {
        'default': LocationDetailSerializer,
        'retrieve': LocationDetailSerializer,
        'list': LocationListSerializer
    }

    def get_queryset(self):
        return Location.objects.filter(is_active=True)

