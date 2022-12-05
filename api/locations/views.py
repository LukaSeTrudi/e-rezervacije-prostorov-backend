
from api.locations.serializers import LocationCourtSerializer, LocationDetailSerializer, LocationListSerializer
from api.mixins import MultipleSerializersMixin
from apps.locations.models import Location, LocationCourt

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class LocationViewSet(MultipleSerializersMixin, viewsets.ReadOnlyModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    serializers = {
        'default': LocationDetailSerializer,
        'retrieve': LocationDetailSerializer,
        'list': LocationListSerializer
    }

    def get_queryset(self):
        return Location.objects.filter(is_active=True)

class LocationCourtViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['location', 'court_types']
    
    serializer_class = LocationCourtSerializer
    def get_queryset(self):
        return LocationCourt.objects.filter(is_active=True)
