from rest_framework import serializers
from rest_framework.generics import GenericAPIView, CreateAPIView
from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse
)
from .user_viewsets import UserModelSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class ChangePasswordReqSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=30)
    new_password = serializers.CharField(max_length=30)

class ChangePasswordResSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Password changed successfully")

class ChangePasswordView(GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ChangePasswordReqSerializer
    queryset = UserModelSerializer.Meta.model.objects.all()

    @extend_schema(
            request=ChangePasswordReqSerializer,
            responses={
                200: ChangePasswordResSerializer,
                400: ChangePasswordResSerializer
                }
    )
    def post(self, request, pk):
        user = self.get_object()
        print(user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_password = serializer.validated_data["old_password"]
        new_password = serializer.validated_data["new_password"]
        if not user.check_password(old_password):
            return Response({"detail": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)