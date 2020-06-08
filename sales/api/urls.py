from django.conf.urls import url

from sales.api.view import *

urlpatterns = [
    url(r'^quotations/$', QuotationAPIView.as_view()),
    url(r'^quotation/(?P<pk>\d+)/$', QuotationDetailAPIView.as_view()),
    url(r'^quote-items/$', QuoteItemAPIView.as_view()),
    url(r'^quote-item/(?P<pk>\d+)/$', QuoteItemDetailAPIView.as_view()),
    url(r'^sales/$', SalesAPIView.as_view()),
    url(r'^sale/(?P<pk>\d+)/$', SalesDetailAPIView.as_view()),
    url(r'^sales-item/$', SalesItemAPIView.as_view()),
    url(r'^sale-item/(?P<pk>\d+)/$', SalesItemDetailAPIView.as_view()),
]
