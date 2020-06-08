from django.contrib.auth.models import User
from django.db import models


class DocumentModel(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

    DOCUMENT_STATUS_CHOICES = (
        (ACTIVE, 'ACTIVE'),
        (INACTIVE, 'INACTIVE'),
    )

    id = models.AutoField(primary_key=True)
    document_status = models.CharField(max_length=200, null=True, choices=DOCUMENT_STATUS_CHOICES, default=ACTIVE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
