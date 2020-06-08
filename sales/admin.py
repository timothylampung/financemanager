from django.contrib import admin

# Register your models here.
from sales.models import Quotation, QuoteItem


class QuotationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'expiry_date',
        'total',
        'status',
        'owner',
        'document_status'
    ]


admin.site.register(Quotation, QuotationAdmin)


class QuoteItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'qi_quotation',
        'subtotal',
        'quantity',
        'offer',
        'owner',
        'document_status'
    ]


admin.site.register(QuoteItem, QuoteItemAdmin)
