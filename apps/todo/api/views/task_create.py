from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.todo.serializers import TaskSerializer


class TaskCreateAPIView(APIView):
    """
        Create a New Task
    """
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
