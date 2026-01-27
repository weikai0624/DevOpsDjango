from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema
from accounts.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import action

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UserViewSets(ModelViewSet):
    queryset = UserModelSerializer.Meta.model.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAdminUser]