from django.contrib.auth import login, authenticate
from rest_framework.generics import GenericAPIView
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework import serializers


class LogoutResSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Successfully logged out")

class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
            summary="Logout(clear Django Session)",
            responses={200: LogoutResSerializer}
    )
    def post(self, request):
        auth.logout(request)
        return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)