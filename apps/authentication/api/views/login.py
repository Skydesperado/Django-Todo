from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.jwt import create_jwt


class UserLoginAPIView(APIView):
    """
        Login a User
    """
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            tokens = create_jwt(user)
            response = {
                "message": "Logged In Successfully",
                "tokens": tokens,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid Email or Password"},
                            status=status.HTTP_404_NOT_FOUND)
