
from apps.schedules.models import CourtReservation, CourtSchedule
from rest_framework import serializers

class CourtScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSchedule
        fields = ('id', 'court', 'day', 'day_formatted', 'start_time', 'end_time', 'price', 'is_active', 'created_at', 'updated_at')

class CourtScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSchedule
        fields = ('court', 'day', 'start_time', 'end_time', 'price', 'is_active')
        extra_kwargs = { 'court': { 'required': False } }

class CourtReservationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtReservation
        fields = ('id', 'schedule', 'user', 'date', 'confirmed', 'created_at', 'updated_at')