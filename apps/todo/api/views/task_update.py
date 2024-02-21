from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer
from permissions.is_owner import IsOwner


class TaskUpdateAPIView(APIView):
    """
        Update an Existing Task
    """
    permission_classes = [
        IsOwner,
    ]

    def put(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except:
            return Response(_("Task With This ID Does Not Found"),
                            status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
