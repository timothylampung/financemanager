from rest_framework import serializers

from offer.models import Offer as OfferModel


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferModel
        fields = '__all__'
