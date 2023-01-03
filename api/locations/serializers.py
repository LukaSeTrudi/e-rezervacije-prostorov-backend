from api.users.serializers import UserListSerializer
from apps.locations.models import CourtType, Location, LocationCourt
from rest_framework import serializers

class LocationListSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ('id', 'name', 'city')

    def get_city(self, obj):
        if obj.city is None:
            return None
        return obj.city.name

class LocationDetailSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ('id', 'name', 'latitude', 'longitude', 'city', 'website_url', 'phone_number', 'email', 'owner', 'created_at', 'updated_at')

    
    def get_city(self, obj):
        if obj.city is None:
            return None
        return obj.city.name

class CourtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtType
        fields = ('id', 'name')

class LocationCourtSerializer(serializers.ModelSerializer):
    court_types = CourtTypeSerializer(many=True)
    location = LocationListSerializer()
    owner = UserListSerializer(source='location.owner.profile')

    class Meta:
        model = LocationCourt
        fields = ('id', 'name', 'location', 'owner', 'court_types', 'is_active', 'created_at', 'updated_at', 'is_outside')