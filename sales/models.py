from datetime import datetime

from django.db import models
from backend.models import DocumentModel
from contacts.models import Customer
from offer.models import Offer


class Quotation(DocumentModel):
    NEW = 'NEW'
    EXPIRED = 'EXPIRED'
    ACCEPTED = 'ACCEPTED'
    CANCELED = 'CANCELED'

    STATUS_CHOICES = (
        (NEW, 'NEW'),
        (ACCEPTED, 'ACCEPTED'),
        (CANCELED, 'CANCELED'),
        (EXPIRED, 'EXPIRED'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=0, related_name='q_customer')
    expiry_date = models.DateTimeField(default=datetime.now, blank=True)
    total = models.FloatField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS_CHOICES, default=NEW)


class QuoteItem(DocumentModel):
    qi_quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, default=0, related_name='qi_quotation')
    subtotal = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, default=0, related_name='offer')


class Sales(DocumentModel):
    PAID = 'PAID'
    PARTIALLY_PAID = 'PARTIALLY_PAID'

    PAYMENT_STATUS = (
        (PAID, 'ACTIVE'),
        (PARTIALLY_PAID, 'PARTIALLY_PAID'),
    )
    s_quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, default=0, related_name='s_quotation')
    payment_status = models.CharField(max_length=200, null=True, choices=PAYMENT_STATUS, default=PARTIALLY_PAID)


class SalesItem(DocumentModel):
    name = models.CharField(max_length=200, null=False)
    subtotal = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    si_sales = models.ForeignKey(Sales, on_delete=models.CASCADE, default=0, related_name='si_sales')
