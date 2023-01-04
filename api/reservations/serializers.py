from apps.schedules.models import CourtReservation, CourtSchedule
from rest_framework import serializers

class CourtScheduleListSerializer(serializers.ModelSerializer):
    day_formatted = serializers.SerializerMethodField()
    class Meta:
        model = CourtSchedule
        fields = ('id', 'court', 'day', 'day_formatted', 'start_time', 'end_time', 'is_active', 'created_at', 'updated_at', 'price')

    def get_day_formatted(self, obj):
        return obj.get_day_display()

class CourtReservationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtReservation
        fields = ('schedule', 'date')

class CourtReservationListSerializer(serializers.ModelSerializer):
    schedule = CourtScheduleListSerializer()

    class Meta:
        model = CourtReservation
        fields = ('id', 'user', 'schedule', 'date', 'confirmed', 'created_at', 'updated_at')
