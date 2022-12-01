from api.locations.serializers import CourtTypeSerializer
from api.users.serializers import UserDetailSerializer, UserListSerializer
from apps.locations.models import Location, LocationCourt
from rest_framework import serializers

class LocationCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Location
        fields = ('name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active')

class LocationListSerializer(serializers.ModelSerializer):
    owner = UserListSerializer(source='owner.profile')
    class Meta:
        model = Location
        fields = ('id', 'name', 'is_active', 'owner')

class LocationDetailSerializer(serializers.ModelSerializer):

    owner = UserDetailSerializer(source='owner.profile')
    class Meta:
        model = Location
        fields = ('id', 'name', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active')

class LocationCourtListSerializer(serializers.ModelSerializer):
    court_types = CourtTypeSerializer(many=True)

    class Meta:
        model = LocationCourt
        fields = ('id', 'name', 'court_types', 'location')

class LocationCourtCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCourt
        fields = ('name', 'court_types', 'location')
        extra_kwargs = { 'location': {'required': False} }

class LocationCourtUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCourt
        fields = ('name', 'court_types')