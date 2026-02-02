from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from django.contrib import auth
from accounts.models import User
from drf_spectacular.utils import extend_schema
from kuop.utils.view import validate_request_serializer
from rest_framework import status
from rest_framework.response import Response

class LoginReqSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=200, required=True)

class LoginResSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Successfully logged in")

class LoginResErSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Failed logged in")

class LoginView(GenericAPIView):
    serializer_class = LoginReqSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Login(with Django Session)",
        request=LoginReqSerializer, 
        responses={
            200: LoginResSerializer,
            400: LoginResErSerializer
        }
    )
    @validate_request_serializer()
    def post(self, request):
        user = auth.authenticate(
            request=request, 
            username=request.validated_data["username"],
            password=request.validated_data["password"]
        )
        if user:
            auth.login(request, user)
            return Response({"detail": "Successfully logged in"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Failed logged in"}, status=status.HTTP_400_BAD_REQUEST)