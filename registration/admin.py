from django.contrib import admin
from .models import Registration, SiteSettings

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'id_number', 'phone', 'application_date', 'agreed_to_terms')
    search_fields = ('full_name', 'id_number', 'phone', 'email')
    list_filter = ('application_date', 'has_driving_license', 'has_sports_license', 'has_previous_experience')

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'registration_open')
