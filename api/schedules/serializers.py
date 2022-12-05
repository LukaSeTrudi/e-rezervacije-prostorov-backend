from datetime import datetime, timedelta
from rest_framework import serializers
from apps.schedules.models import CourtReservation, CourtSchedule

class CourtScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSchedule
        fields = ('id', 'court', 'day', 'day_formatted', 'start_time', 'end_time', 'price', 'created_at', 'updated_at')

class CourtReservationsSerializer(serializers.ModelSerializer):
    reservation_taken = serializers.SerializerMethodField()
    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = CourtSchedule
        fields = ('id', 'court', 'date','reservation_taken', 'start_datetime', 'end_datetime', 'day', 'day_formatted', 'start_time', 'end_time', 'price', 'created_at', 'updated_at')
    
    def get_date(self, obj):
        date = self.context['date']
        return date

    def get_reservation_taken(self, obj):
        date = self.context['date']
        current_user = self.context['user']

        date_true = date + timedelta(days=int(obj.day) - 1)
        print(date_true)
        reservation = CourtReservation.objects.filter(schedule=obj, date=date_true)
        if reservation.exists():
            return False if reservation.first().user == current_user else True
        return False
    
    def get_start_datetime(self, obj):
        date = self.context['date']
        date = datetime.combine(date, obj.start_time)
        return date + timedelta(days=int(obj.day) - 1)
    
    def get_end_datetime(self, obj):
        date = self.context['date']
        date = datetime.combine(date, obj.end_time)
        return date + timedelta(days=int(obj.day) - 1)