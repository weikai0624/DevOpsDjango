from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from drf_spectacular.utils import extend_schema

class JwtTokenRefresh(TokenRefreshView):

    @extend_schema(
            summary="Token Refresh(with JWT token)",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)