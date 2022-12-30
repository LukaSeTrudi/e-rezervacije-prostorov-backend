
from api.mixins import MultipleSerializersMixin
from api.users.serializers import UserUpdateSerializer, UserDetailSerializer, UserListSerializer
from api.users.permissions import IsUserOrReadOnly
from apps.profiles.models import UserProfile
from apps.logs.models import Log

from rest_framework import viewsets, mixins, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(MultipleSerializersMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    # Only alloweed to update your own profile, and view other profiles
    permission_classes = (IsUserOrReadOnly,)

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    filterset_fields = ['is_company']

    lookup_field = "user__pk"

    serializers = {
        'default': UserDetailSerializer,
        'retrieve': UserDetailSerializer,
        'list': UserListSerializer,
        'create': None,
        'update': UserUpdateSerializer,
    }

    def get_queryset(self):
        return UserProfile.objects.filter(is_active=True)
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            for instance in page:
                Log.objects.create(
                    user=self.request.user,
                    user_profile=instance,
                    log_type=Log.LOG_TYPE_USER_PROFILE_SHOWN
                )
            
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Log.objects.create(
            user=self.request.user,
            user_profile=instance,
            log_type=Log.LOG_TYPE_USER_PROFILE_DETAIL
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False, url_path='current')
    def current_user(self, request):
        return Response(UserDetailSerializer(request.user.profile).data)