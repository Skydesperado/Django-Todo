from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from apps.authentication.models import User
from apps.todo.models import Task


class TestTaskListAPIView(TestCase):
    """
        Test Cases For Task List API View
    """
    def setUp(self):
        """
            Set Up Test Data
        """
        self.client = APIClient()
        self.user = baker.make(User)
        self.url = reverse("todo:task-list-view",
                           kwargs={"uuid": self.user.uuid})

    def test_anonymous_user(self):
        """
            Test That Anonymous Users Cannot Access The Task List View
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_without_task(self):
        """
            Test For Authenticated Users Without Tasks
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authenticated_user_with_task(self):
        """
            Test For Authenticated Users With Tasks
        """
        tasks = baker.make(Task, user=self.user, _quantity=10)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_without_permission(self):
        """
            Test For Another User Attempting To Access The Data of Another User
        """
        random_user = baker.make(User)
        self.client.force_authenticate(user=random_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
