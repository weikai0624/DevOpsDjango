from django.urls import (
    path,
    include,
)
from .user.user_viewsets import UserViewSets
from .user.change_password import ChangePasswordView
from .user.logout import LogoutView
from .user.login import LoginView

from .user.jwt.token import JwtToken
from .user.jwt.token_refresh import JwtTokenRefresh
from .user.jwt.token_verify import JwtTokenVerify

urlpatterns = [
    path('user/', UserViewSets.as_view({
            "get": "list",
        }
    )),
    path('user/<int:pk>/', UserViewSets.as_view({
            "get": "retrieve",
            "delete": "destroy",
        }
    )),
    path('user/<int:pk>/change_password/', ChangePasswordView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('jwttoken/', JwtToken.as_view(), name='token_obtain_pair'),
    path('jwttoken/refresh/', JwtTokenRefresh.as_view(), name='token_refresh'),
    path('jwttoken/verify/', JwtTokenVerify.as_view(), name='token_verify'),
]
