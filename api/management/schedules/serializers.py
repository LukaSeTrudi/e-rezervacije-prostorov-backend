
from apps.schedules.models import CourtReservation, CourtSchedule
from rest_framework import serializers

class CourtScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSchedule
        fields = ('id', 'court', 'day', 'title', 'day_formatted', 'start_time', 'end_time', 'price', 'is_active', 'created_at', 'updated_at')

class CourtScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSchedule
        fields = ('court', 'day', 'title', 'start_time', 'end_time', 'price', 'is_active')
        extra_kwargs = { 'court': { 'required': False } }

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('Start time must be before end time.')
        return data

class CourtReservationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtReservation
        fields = ('id', 'schedule', 'user', 'date', 'confirmed', 'created_at', 'updated_at')