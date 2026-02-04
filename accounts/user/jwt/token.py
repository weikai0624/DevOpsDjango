from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class JwtToken(TokenObtainPairView):

    @extend_schema(
            summary="Login(with JWT token)",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

