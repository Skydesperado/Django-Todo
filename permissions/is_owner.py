from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from apps.authentication.models import User
from apps.todo.models import Task


class IsOwner(BasePermission):
    message = _("Permission Denied")

    def has_permission(self, request, view):
        try:
            if "id" in request.parser_context["kwargs"]:
                task_id = request.parser_context["kwargs"]["id"]
                try:
                    task = Task.objects.get(id=task_id)
                    if request.user.is_authenticated and request.user == task.user:
                        return True
                except Task.DoesNotExist:
                    return Response(_("Task With This ID Does Not Found"),
                                    status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            pass
        try:
            if "uuid" in request.parser_context["kwargs"]:
                user_uuid = request.parser_context["kwargs"]["uuid"]
                try:
                    user = User.objects.get(uuid=user_uuid)
                    if request.user.is_authenticated and request.user == user:
                        return True
                except User.DoesNotExist:
                    return Response(_("User With This UUID Does Not Exist"),
                                    status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            pass
        return False
