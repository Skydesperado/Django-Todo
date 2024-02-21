from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authentication.api.views.login import UserLoginAPIView
from apps.authentication.api.views.register import UserRegistrationAPIView

from .jwt import CustomTokenObtainPairView

app_name = "authentication"

urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="register-view"),
    path("login/", UserLoginAPIView.as_view(), name="login-view"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token-view"),
    path("token/refresh/",
         TokenRefreshView.as_view(),
         name="token-refresh-view"),
]
