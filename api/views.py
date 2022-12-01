from api.locations.serializers import CourtTypeSerializer
from apps.locations.models import CourtType
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CourtTypeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response(CourtTypeSerializer(CourtType.objects.all(), many=True).data)