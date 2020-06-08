from django.contrib import admin

# Register your models here.
from contacts.models import Customer, Provider


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'phone_no',
    ]


class ProviderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'phone_no',
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Provider, ProviderAdmin)
