from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.authentication.models import User


class Task(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name=_("User"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("Description"))
    is_completed = models.BooleanField(default=False,
                                       blank=True,
                                       null=True,
                                       verbose_name=_("Completed"))

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return f"{self.user} - {self.title} - {self.is_completed}"
