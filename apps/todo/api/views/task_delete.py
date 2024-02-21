from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.todo.models import Task
from permissions.is_owner import IsOwner


class TaskDeleteAPIView(APIView):
    """
        Delete a Task
    """
    permission_classes = [
        IsOwner,
    ]

    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except:
            return Response(_("Task With This ID Does Not Found"),
                            status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(_("Task Deleted"), status=status.HTTP_204_NO_CONTENT)
