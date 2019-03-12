from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^openid/', include('oidc_provider.urls', namespace='oidc_provider')),
]
