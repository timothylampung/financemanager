from django.db import models

from backend.models import DocumentModel


class Offer(DocumentModel):
    PRODUCT = 'PRODUCT'
    SERVICE = 'SERVICE'

    OFFER_OPTIONS = (
        (PRODUCT, 'PRODUCT'),
        (SERVICE, 'SERVICE'),
    )

    ref_no = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    offer_type = models.CharField(max_length=200, null=True, choices=OFFER_OPTIONS, default=PRODUCT)
    unit = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    reserved_quantity = models.IntegerField(blank=True, null=True)
    purchase_price = models.FloatField(null=True)
    sale_price = models.FloatField(null=False)
