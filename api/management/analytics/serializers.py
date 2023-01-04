from apps.locations.models import Location, LocationCourt
from apps.profiles.models import UserProfile
from rest_framework import serializers
from apps.logs.models import Log

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'full_name')
class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCourt
        fields = ('id', 'name')


class LogListSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    court = CourtSerializer()
    user_profile = UserProfileSerializer()

    user = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = ('id', 'user', 'log_type', 'created_at', 'location', 'court', 'user_profile')

    def get_user(self, obj):
        if obj.user_profile is None:
            return None
        return obj.user_profile.user.username