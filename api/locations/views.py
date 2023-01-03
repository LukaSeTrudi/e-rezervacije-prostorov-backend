
from api.locations.serializers import LocationCourtSerializer, LocationDetailSerializer, LocationListSerializer
from api.mixins import MultipleSerializersMixin
from apps.locations.models import Location, LocationCourt
from apps.logs.models import Log
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

class LocationViewSet(MultipleSerializersMixin, viewsets.ReadOnlyModelViewSet):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['owner']
    
    serializers = {
        'default': LocationDetailSerializer,
        'retrieve': LocationDetailSerializer,
        'list': LocationListSerializer
    }

    def get_queryset(self):
        return Location.objects.filter(is_active=True)
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            for location in page:
                print(location)
                Log.objects.create(
                    user=self.request.user,
                    location=location,
                    log_type=Log.LOG_TYPE_LOCATION_SHOWN
                )
            
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Log.objects.create(
            user=self.request.user,
            location=instance,
            log_type=Log.LOG_TYPE_LOCATION_DETAIL
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class LocationCourtViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'location__city__name']
    filterset_fields = ['location', 'court_types', 'is_outside']
    
    serializer_class = LocationCourtSerializer
    def get_queryset(self):
        qs = LocationCourt.objects.filter(is_active=True)
        if self.request.user.is_authenticated:
            for court in qs:
                Log.objects.create(
                    user=self.request.user,
                    court=court,
                    log_type=Log.LOG_TYPE_COURT_SHOWN
                )
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            for court in page:
                Log.objects.create(
                    user=self.request.user,
                    court=court,
                    log_type=Log.LOG_TYPE_COURT_SHOWN
                )
            
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Log.objects.create(
            user=self.request.user,
            court=instance,
            log_type=Log.LOG_TYPE_COURT_DETAIL
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)