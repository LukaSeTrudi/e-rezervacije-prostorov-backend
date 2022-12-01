
from api.extensions import LocationMixin
from api.management.permissions import IsOwner
from api.management.locations.serializers import LocationCourtCreateSerializer, LocationCourtListSerializer, LocationCourtUpdateSerializer, LocationDetailSerializer, LocationCreateSerializer, LocationListSerializer
from api.mixins import MultipleSerializersMixin
from apps.locations.models import Location

from rest_framework import viewsets


class LocationViewSet(MultipleSerializersMixin, viewsets.ModelViewSet):
    permission_classes = (IsOwner, )
    serializers = {
        'default': LocationDetailSerializer,
        'retrieve': LocationDetailSerializer,
        'create': LocationCreateSerializer,
        'update': LocationCreateSerializer,
        'list': LocationListSerializer
    }

    def get_queryset(self):
        return Location.objects.filter(owner=self.request.user)

class LocationCourtViewSet(MultipleSerializersMixin, LocationMixin, viewsets.ModelViewSet):
    permission_classes = (IsOwner, )
    serializers = {
        'default': LocationCourtListSerializer,
        'retrieve': LocationCourtListSerializer,
        'create': LocationCourtCreateSerializer,
        'update': LocationCourtUpdateSerializer,
        'list': LocationCourtListSerializer
    }

    def get_queryset(self):
        return self.get_location().courts.all()

    def perform_create(self, serializer):
        serializer.save(location=self.get_location())

    def perform_update(self, serializer):
        serializer.save(location=self.get_location())