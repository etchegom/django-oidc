from django.contrib.admin import ModelAdmin
from django.contrib import admin
from oidc_provider.models import UserConsent


@admin.register(UserConsent)
class UserConsentAdmin(ModelAdmin):
    pass
