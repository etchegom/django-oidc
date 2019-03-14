from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^', include('oidc_provider.urls', namespace='oidc_provider')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
