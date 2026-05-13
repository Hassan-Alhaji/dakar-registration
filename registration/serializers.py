from rest_framework import serializers
from .models import Registration, RegistrationStats

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        read_only_fields = ['status', 'application_date', 'updated_date', 'reviewed_date', 'admin_notes', 'reviewed_by']

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationStats
        fields = '__all__'
