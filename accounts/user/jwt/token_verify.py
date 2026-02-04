from rest_framework_simplejwt.views import (
    TokenVerifyView,
)
from drf_spectacular.utils import extend_schema

class JwtTokenVerify(TokenVerifyView):
    @extend_schema(
            summary="Token Verify(with JWT token)",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)