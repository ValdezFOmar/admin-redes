from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self) -> str:
        return f"id<{self.id}> {self.username}"


class Ticket(models.Model):
    """Defines a single issue, either hardware or software."""

    user = models.ForeignKey(User, models.CASCADE, "tickets", blank=True)
    issue_date = models.DateField(blank=False)
    reported_date = models.DateTimeField(blank=True)
    description = models.TextField(max_length=1024, blank=False)
    is_solved = models.BooleanField(default=False)
    assignee = models.ForeignKey(User, models.SET_NULL, "asigned_tickets", null=True, blank=True)

    class Meta:
        ordering = ["-reported_date"]
        get_latest_by = "reported_date"

    def __str__(self):
        return f"({self.user.username}): {self.description}"
