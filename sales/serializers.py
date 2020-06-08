from rest_framework import serializers

from sales.models import \
    Quotation as QuotationModel, \
    QuoteItem as QuoteItemModel, \
    Sales as SalesModel, \
    SalesItem as SalesItemModel


class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationModel
        fields = '__all__'


class QuoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteItemModel
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesModel
        fields = '__all__'


class SalesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItemModel
        fields = '__all__'
