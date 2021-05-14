from django.db import models
from django.contrib.auth.models import User, Group


class Ticket(models.Model):

    class Impact(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
        related_name='ticket_author')
    title = models.TextField()
    description = models.TextField(blank=True)
    impact = models.IntegerField(choices=Impact.choices)
    category = models.TextField(blank=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
        related_name='ticket_assignee')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
