import uuid
from django.db import models
from django.utils import timezone


class Timeline(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    start = models.DateTimeField()
    stop = models.DateTimeField(
        null=True,
        default=None,
    )
    user = models.ForeignKey(
        'account.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
