from rest_framework import generics, mixins

from sales.models import Quotation, QuoteItem, Sales, SalesItem
from sales.serializers import QuotationSerializer, QuoteItemSerializer, SalesSerializer, SalesItemSerializer


class QuotationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

    def get_queryset(self):
        qs = Quotation.objects.filter(owner=self.request.user)
        query = self.request.GET.get('query')
        if query is not None:
            qs = qs.filter(name__contains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QuotationDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

    def get_queryset(self):
        return Quotation.objects.filter(owner=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuoteItemAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = QuoteItem.objects.all()
    serializer_class = QuoteItemSerializer

    def get_queryset(self):
        qs = QuoteItem.objects.filter(owner=self.request.user)
        query = self.request.GET.get('query')
        if query is not None:
            qs = qs.filter(name__contains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QuoteItemDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = QuoteItem.objects.all()
    serializer_class = QuoteItemSerializer

    def get_queryset(self):
        return QuoteItem.objects.filter(owner=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SalesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    def get_queryset(self):
        qs = Sales.objects.filter(owner=self.request.user)
        query = self.request.GET.get('query')
        if query is not None:
            qs = qs.filter(name__contains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SalesDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    def get_queryset(self):
        return Sales.objects.filter(owner=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SalesItemAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer

    def get_queryset(self):
        qs = SalesItem.objects.filter(owner=self.request.user)
        query = self.request.GET.get('query')
        if query is not None:
            qs = qs.filter(name__contains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SalesItemDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer

    def get_queryset(self):
        return SalesItem.objects.filter(owner=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
