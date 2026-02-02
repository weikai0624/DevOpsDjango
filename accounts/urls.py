from django.urls import (
    path,
    include,
)
from .user.user_viewsets import UserViewSets
from .user.change_password import ChangePasswordView
from .user.logout import LogoutView
from .user.login import LoginView

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
]
