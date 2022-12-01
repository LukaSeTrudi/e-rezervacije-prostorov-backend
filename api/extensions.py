from apps.locations.models import Location
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