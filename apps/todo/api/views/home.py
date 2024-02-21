from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeAPIView(APIView):
    """
        Show Homepage
    """
    permission_classes = [
        AllowAny,
    ]

    def get(self, request):
        return Response(
            data={"message": "This Is The Homepage of Our Todo API"},
            status=status.HTTP_200_OK)
