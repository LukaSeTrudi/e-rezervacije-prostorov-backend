from api.locations.serializers import CourtTypeSerializer
from api.users.serializers import UserDetailSerializer, UserListSerializer
from apps.locations.models import Location, LocationCourt, LocationCity
from rest_framework import serializers

class LocationCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCity
        fields = ('id', 'name')

class LocationCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Location
        fields = ('name', 'latitude', 'longitude', 'city', 'owner', 'website_url', 'phone_number', 'email', 'is_active')

class LocationListSerializer(serializers.ModelSerializer):
    owner = UserListSerializer(source='owner.profile')
    city = LocationCitySerializer()

    class Meta:
        model = Location
        fields = ('id', 'name', 'is_active', 'owner', 'city')

class LocationDetailSerializer(serializers.ModelSerializer):
    city = LocationCitySerializer()
    owner = UserDetailSerializer(source='owner.profile')
    class Meta:
        model = Location
        fields = ('id', 'name', 'city', 'latitude', 'longitude', 'owner', 'website_url', 'phone_number', 'email', 'is_active')

class LocationCourtListSerializer(serializers.ModelSerializer):
    court_types = CourtTypeSerializer(many=True)

    class Meta:
        model = LocationCourt
        fields = ('id', 'name', 'court_types', 'location', 'is_outside', 'is_active')

class LocationCourtCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCourt
        fields = ('name', 'court_types', 'location', 'is_outside', 'is_active')
        extra_kwargs = { 'location': {'required': False} }

class LocationCourtUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCourt
        fields = ('name', 'court_types', 'is_outside', 'is_active')