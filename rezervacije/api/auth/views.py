from django.shortcuts import render
from api.auth.serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
# Create your views here.

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)