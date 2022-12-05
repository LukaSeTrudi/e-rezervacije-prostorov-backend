
from datetime import timedelta
from api.schedules.serializers import CourtReservationsSerializer, CourtScheduleListSerializer
from apps.schedules.models import CourtSchedule
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

import calendar

class CourtScheduleAPIView(APIView):
    def get(self, request):
        params = request.query_params
        if 'date' in params:
            date = timezone.datetime.strptime(params['date'], "%Y-%m-%d").date()
        else:
            date = timezone.now().date()
        queryset = CourtSchedule.objects.filter(is_active=True)
        if 'location' in params:
            queryset = queryset.filter(court__location=params['location'])
        if 'court' in params:
            queryset = queryset.filter(court=params['court'])
        if 'day' in params:
            queryset = queryset.filter(day=params['day'])
            return Response(CourtReservationsSerializer(queryset, many=True, context={'date': date - timedelta(days=date.weekday()), 'user': request.user}).data)
        
        month = params.get('month', None)
        if month is not None:
            response = []
            start_date = date - timedelta(days=date.weekday())
            delta = timedelta(weeks=1)
            for i in range(6):
                response.append(CourtReservationsSerializer(queryset, many=True, context={'date': start_date, 'user': request.user}).data)
                start_date = start_date + delta
        else:
            start_week = date - timedelta(days=date.weekday())
            response = CourtReservationsSerializer(queryset, many=True, context={ 'date': start_week, 'user': request.user }).data

        
        return Response(response)
