from api.locations.serializers import CourtTypeSerializer
from api.serializers import LocationCitySerializer
from apps.locations.models import CourtType, LocationCity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CourtTypeAPIView(APIView):
    permission_classes = []

    def get(self, request, format=None):
        if CourtType.objects.all().count() == 0:
            CourtType.objects.create(name="Tennis")
            CourtType.objects.create(name="Squash")
            CourtType.objects.create(name="Basketball")
            CourtType.objects.create(name="Volleyball")
            CourtType.objects.create(name="Badminton")
            CourtType.objects.create(name="Table Tennis")
            CourtType.objects.create(name="Football")
            CourtType.objects.create(name="Handball")
            CourtType.objects.create(name="Other")

        return Response(CourtTypeSerializer(CourtType.objects.all(), many=True).data)

class CityAPIView(APIView):
    permission_classes = []

    def get(self, request, format=None):
        return Response(LocationCitySerializer(LocationCity.objects.all(), many=True).data)
