from apps.locations.models import Location, LocationCourt
from apps.schedules.models import CourtSchedule
from rest_framework.generics import get_object_or_404


class LocationMixin():
    def get_location(self):
        qs = Location.objects.all()

        location_pk = self.kwargs.get('location_pk', None)

        filter_kwargs = {
            'pk': location_pk
        }

        obj = get_object_or_404(qs, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class CourtMixin(LocationMixin):
    def get_court(self):
        qs = LocationCourt.objects.filter(location=self.get_location())

        court_pk = self.kwargs.get('court_pk', None)

        filter_kwargs = {
            'pk': court_pk
        }

        obj = get_object_or_404(qs, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class ScheduleMixin(CourtMixin):
    def get_schedule(self):
        qs = CourtSchedule.objects.filter(court=self.get_court())

        schedule_pk = self.kwargs.get('schedule_pk', None)

        filter_kwargs = {
            'pk': schedule_pk
        }

        obj = get_object_or_404(qs, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj