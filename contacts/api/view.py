from rest_framework import generics, mixins
from contacts.models import Customer
from contacts.serializer import CustomerSerializer


class CustomerAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        qs = Customer.objects.filter(owner=self.request.user)
        query = self.request.GET.get('query')
        if query is not None:
            qs = qs.filter(name__contains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomerDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.filter(owner=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
