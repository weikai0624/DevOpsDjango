from django.urls import (
    path,
    include,
)
from .user.user_viewsets import UserViewSets
from .user.change_password import ChangePasswordView

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
    path('user/<int:pk>/change_password/', ChangePasswordView.as_view())
]
