from django.contrib.auth.models import User
from django.db import models

from backend.models import DocumentModel


class Provider(DocumentModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    phone_no = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Customer(DocumentModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    phone_no = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
