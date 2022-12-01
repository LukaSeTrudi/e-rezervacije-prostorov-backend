from rest_framework import status
from rest_framework.response import Response

class MultipleSerializersMixin:
    serializers = {
        'default': None,
        'retrieve': None,
        'create': None,
        'update': None,
        'list': None
    }

    def get_serializer_class(self):
        action = self.action
        if action == 'partial_update':
            action = 'update'

        return self.serializers.get(action, self.serializers['default'])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        response_serializer = self.serializers.get('retrieve', self.serializers['default'])(serializer.instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        response_serializer = self.serializers.get('retrieve', self.serializers['default'])(serializer.instance)
        return Response(response_serializer.data)
