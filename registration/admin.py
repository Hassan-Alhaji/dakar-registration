from django.contrib import admin
from .models import Registration, SiteSettings

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_id', 'mobile_number', 'application_date')
    search_fields = ('first_name', 'last_name', 'national_id', 'mobile_number', 'email')
    list_filter = ('application_date', 'has_driving_license', 'has_sports_license', 'has_previous_experience')

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_registration_open')
