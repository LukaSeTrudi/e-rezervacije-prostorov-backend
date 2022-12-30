from apps.locations.models import Location, LocationCourt
from apps.schedules.models import CourtSchedule
from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated or not request.user.profile.is_company:
            return False

        if obj.__class__ == Location:
            return obj.owner == request.user
        elif obj.__class__ == LocationCourt:
            return obj.location.owner == request.user
        elif obj.__class__ == CourtSchedule:
            return obj.court.location.owner == request.user
        return True