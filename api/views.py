from api.locations.serializers import CourtTypeSerializer
from api.serializers import LocationCitySerializer
from apps.locations.models import CourtType, LocationCity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CourtTypeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response(CourtTypeSerializer(CourtType.objects.all(), many=True).data)

class CityAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response(LocationCitySerializer(LocationCity.objects.all(), many=True).data)
