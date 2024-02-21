from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from apps.authentication.models import User
from apps.todo.models import Task


class TestTaskDetailAPIView(TestCase):
    """
        Test Cases For Task Detail API View
    """
    def setUp(self):
        """
            Set Up Test Data
        """
        self.client = APIClient()
        self.user = baker.make(User)
        self.task = baker.make(Task, user=self.user)
        self.url = reverse("todo:task-detail-view",
                           kwargs={"id": self.task.id})

    def test_anonymous_user(self):
        """
            Test That Anonymous Users Cannot Access The Task Detail View
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_task_existent(self):
        """
            Test That a Task With The Given ID Exists
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse("todo:task-detail-view", kwargs={"id": 2}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authenticated_user_without_permission(self):
        """
            Test For Another User Attempting To Access The Data of Another User
        """
        random_user = baker.make(User)
        self.client.force_authenticate(user=random_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
