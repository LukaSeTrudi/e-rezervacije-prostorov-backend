
from api.extensions import LocationMixin, CourtMixin, ScheduleMixin
from api.management.permissions import IsOwner
from api.management.schedules.serializers import CourtReservationListSerializer, CourtScheduleListSerializer, CourtScheduleCreateSerializer
from api.mixins import MultipleSerializersMixin
from apps.schedules.models import CourtReservation, CourtSchedule

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class CourtScheduleViewSet(MultipleSerializersMixin, CourtMixin, viewsets.ModelViewSet):
    permission_classes = (IsOwner, )

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['day', 'is_active']
    
    serializers = {
        'default': CourtScheduleListSerializer,
        'retrieve': CourtScheduleListSerializer,
        'create': CourtScheduleCreateSerializer,
        'update': CourtScheduleCreateSerializer,
        'list': CourtScheduleListSerializer
    }

    def get_queryset(self):
        return CourtSchedule.objects.filter(court=self.get_court())
    
    def perform_create(self, serializer):
        serializer.save(court=self.get_court())

    def perform_update(self, serializer):
        serializer.save(court=self.get_court())

class CourtReservationViewSet(ScheduleMixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsOwner, )
    serializer_class = CourtReservationListSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'date', 'confirmed']

    def get_queryset(self):
        return CourtReservation.objects.filter(schedule=self.get_schedule())
