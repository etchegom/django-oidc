from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^', include('oidc_provider.urls', namespace='oidc_provider')),
    path('admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
]
