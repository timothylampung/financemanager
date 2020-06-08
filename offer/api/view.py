from rest_framework import generics, mixins

from offer.models import Offer
from offer.serializers import OfferSerializer


class OfferAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_queryset(self):
        qs = Offer.objects.filter(owner=self.request.user)
        query = self.request.GET.get('query')
        if query is not None:
            qs = qs.filter(name__contains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OfferDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_queryset(self):
        return Offer.objects.filter(owner=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
