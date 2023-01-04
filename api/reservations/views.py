
from api.mixins import MultipleSerializersMixin
from api.reservations.serializers import CourtReservationListSerializer, CourtReservationCreateSerializer
from apps.schedules.models import CourtReservation, CourtSchedule
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action

class ReservationViewSet(MultipleSerializersMixin, viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['schedule__court__name', 'schedule__title']
    filterset_fields = ['schedule__day']
    
    serializers = {
        'default': CourtReservationListSerializer,
    }

    def get_queryset(self):
        return CourtReservation.objects.filter(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        return Response({'status': 'error', 'message': 'Updating reservations is not allowed.'}, status=400)
    def partial_update(self, request, *args, **kwargs):
        return Response({'status': 'error', 'message': 'Updating reservations is not allowed.'}, status=400)

    def create(self, request, *args, **kwargs):
        validator = CourtReservationCreateSerializer(data=request.POST)
        if not validator.is_valid():
            return Response({'status': 'error', 'message': validator.errors}, status=400)

        schedule = validator.validated_data['schedule']
        date = validator.validated_data['date']

        if int((date.weekday() + 1) % 8) != int(schedule.day):
            return Response({'status': 'error', 'message': 'The selected date does not match the schedule.'}, status=400)

        reservation = validator.save(user=request.user)
        reservation.save()
        
        return Response(CourtReservationListSerializer(reservation).data)
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'status': 'success', 'message': 'Reservation deleted successfully.'})