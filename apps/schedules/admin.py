from django.contrib import admin

# Register your models here.
from apps.schedules.models import CourtSchedule, CourtReservation

class CourtScheduleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'day', 'start_time', 'end_time', 'is_active']

class CourtReservationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'date']

admin.site.register(CourtSchedule, CourtScheduleAdmin)
admin.site.register(CourtReservation, CourtReservationAdmin)