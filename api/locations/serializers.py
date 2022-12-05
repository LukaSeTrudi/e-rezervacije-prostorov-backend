from apps.locations.models import CourtType, Location, LocationCourt
from rest_framework import serializers

class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')

class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'latitude', 'longitude', 'website_url', 'phone_number', 'email', 'owner', 'created_at', 'updated_at')

class CourtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtType
        fields = ('id', 'name')

class LocationCourtSerializer(serializers.ModelSerializer):
    court_types = CourtTypeSerializer(many=True)
    class Meta:
        model = LocationCourt
        fields = ('id', 'name', 'location', 'court_types', 'is_active', 'created_at', 'updated_at', 'is_outside')