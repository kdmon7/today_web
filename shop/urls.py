from django.urls import include, path
from . import views

app_name = 'shop'
urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls'))
]