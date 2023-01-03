
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.logs.models import Log
from api.management.analytics.serializers import LogListSerializer

from django.db.models import Q

class AnalyticsAPIView(APIView):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'User not authenticated'}, status=401)
        if not user.profile.is_company:
            return Response({'error': 'User is not a company'}, status=401)

        params = request.query_params
        qs = Log.objects.all()
        if 'type' in params:
            valid_types = [t[0] for t in Log.LOG_TYPES]
            if not params['type'] in valid_types:
                return Response({'error': 'Invalid type, valid types are ' + str.join(', ', valid_types)}, status=400)
            qs = Log.objects.filter(log_type=params['type'])
        
        qs = qs.filter(Q(location=None) | Q(location__owner=user))
        qs = qs.filter(Q(court=None) | Q(court__location__owner=user))
        qs = qs.filter(Q(user_profile=None) | Q(user_profile__user=user))
        
        if 'location' in params:
            qs = qs.filter(location=params['location'])
        if 'court' in params:
            qs = qs.filter(court=params['court'])
        if 'user' in params:
            qs = qs.filter(user_profile=params['user'])

        data = LogListSerializer(qs, many=True).data
        
        return Response(data)