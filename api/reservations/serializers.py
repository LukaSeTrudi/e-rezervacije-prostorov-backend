from apps.schedules.models import CourtReservation, CourtSchedule
from apps.locations.models import LocationCourt, Location
from rest_framework import serializers

class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCourt
        fields = ('id', 'name')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', )

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
    court = CourtSerializer(source='schedule.court')
    location = LocationSerializer(source='schedule.court.location')

    class Meta:
        model = CourtReservation
        fields = ('id', 'court', 'location', 'user', 'schedule', 'date', 'confirmed', 'created_at', 'updated_at')
