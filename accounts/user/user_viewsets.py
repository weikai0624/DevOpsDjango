from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema
from accounts.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UserFilter(filters.FilterSet):
    username = filters.CharFilter(field_name="username", lookup_expr="icontains")
    class Meta:
        model = User
        fields = ['username']

class UserViewSets(ModelViewSet):
    queryset = UserModelSerializer.Meta.model.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = UserFilter
    ordering_fields = ['id', 'username', 'date_joined']
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset()
        # return self.queryset.filter(is_active=False)