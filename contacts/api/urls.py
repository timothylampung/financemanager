from django.conf.urls import url

from contacts.api.view import CustomerAPIView, CustomerDetailAPIView

urlpatterns = [
    url(r'^$', CustomerAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', CustomerDetailAPIView.as_view()),
    # url(r'^(?P<recipe_id>\d+)/instructions/$', InstructionAPIView.as_view()),
    # url(r'^instructions/(?P<instruction_id>\d+)/$', InstructionDetailAPIView.as_view()),
]
