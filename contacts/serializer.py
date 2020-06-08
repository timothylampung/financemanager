from contacts.models import Provider as ProviderModel, Customer as CustomerModel
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderModel
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'
