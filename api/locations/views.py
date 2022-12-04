
from api.locations.serializers import LocationDetailSerializer, LocationListSerializer
from api.mixins import MultipleSerializersMixin
from apps.locations.models import Location

from rest_framework import viewsets, filters


class LocationViewSet(MultipleSerializersMixin, viewsets.ReadOnlyModelViewSet):
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name']
    
    serializers = {
        'default': LocationDetailSerializer,
        'retrieve': LocationDetailSerializer,
        'list': LocationListSerializer
    }

    def get_queryset(self):
        return Location.objects.filter(is_active=True)

