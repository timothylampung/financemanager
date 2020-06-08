from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from financemanager.view import CreateUserView

schema_view = get_swagger_view(title='Finance Manager API')

admin.site.site_header = 'Finance Manager'
admin.site.site_title = 'Finance Manager'
admin.site.index_title = 'Finance Manager'
urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    url('auth-api/jwt/', obtain_jwt_token),
    url(r'^auth-api/register/$', CreateUserView.as_view()),
    url('auth-api/jwt/refresh/', refresh_jwt_token),
    url('contact-api/', include('contacts.urls')),
    url('sales-api/', include('sales.urls')),
    url('offer-api/', include('offer.urls')),
]
