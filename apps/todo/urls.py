from django.urls import path

from apps.todo.api.views.home import HomeAPIView
from apps.todo.api.views.task_create import TaskCreateAPIView
from apps.todo.api.views.task_delete import TaskDeleteAPIView
from apps.todo.api.views.task_detail import TaskDetailAPIView
from apps.todo.api.views.task_list import TaskListAPIView
from apps.todo.api.views.task_update import TaskUpdateAPIView

app_name = "todo"

urlpatterns = [
    path("", HomeAPIView.as_view(), name="home-view"),
    path("todo/<uuid:uuid>/", TaskListAPIView.as_view(),
         name="task-list-view"),
    path("todo/<int:id>/",
         TaskDetailAPIView.as_view(),
         name="task-detail-view"),
    path("todo/create/", TaskCreateAPIView.as_view(), name="task-create-view"),
    path("todo/update/<int:id>/",
         TaskUpdateAPIView.as_view(),
         name="task-update-view"),
    path("todo/delete/<int:id>/",
         TaskDeleteAPIView.as_view(),
         name="task-delete-view"),
]
