from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from apps.authentication.models import User
from apps.todo.models import Task
