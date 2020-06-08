from django.contrib import admin

# Register your models here.
from offer.models import Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = [
        'ref_no',
        'name',
        'offer_type',
        'unit',
        'quantity',
        'reserved_quantity',
        'purchase_price',
        'sale_price',
    ]


admin.site.register(Offer, OfferAdmin)
