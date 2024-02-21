from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models import User
from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer
from permissions.is_owner import IsOwner


class TaskListAPIView(APIView):
    """
    Show Existing Task(s) as a List
    """
    permission_classes = [
        IsOwner,
    ]

    def get(self, request, uuid):
        try:
            user = User.objects.get(uuid=uuid)
        except User.DoesNotExist:
            return Response(_("User With This UUID Does Not Found"),
                            status=status.HTTP_404_NOT_FOUND)
        tasks = Task.objects.filter(user=user)
        if tasks.count() == 0:
            return Response(_("Tasks For The Given User Are Not Found"),
                            status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
