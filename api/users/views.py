
from api.mixins import MultipleSerializersMixin
from api.users.serializers import UserUpdateSerializer, UserDetailSerializer, UserListSerializer
from api.users.permissions import IsUserOrReadOnly
from apps.profiles.models import UserProfile

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
    
    
    @action(methods=['get'], detail=False, url_path='current')
    def current_user(self, request):
        return Response(UserDetailSerializer(request.user.profile).data)