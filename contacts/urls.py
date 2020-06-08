from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    # path('recipes', views.recipes, name='index'),
    # path('recipe', views.recipes_details),
    # path('instructions', views.instructions, name='index'),
    # path('instruction', views.instruction_details),
    url(r'', include('contacts.api.urls'))
]
