from django.conf.urls import url

from offer.api.view import *

urlpatterns = [
    url(r'^offers/$', OfferAPIView.as_view()),
    url(r'^offer/(?P<pk>\d+)/$', OfferDetailAPIView.as_view()),
]
