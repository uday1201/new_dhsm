from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers

class family_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = family_profile
        fields = '__all__'

class basic_amenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = basic_amenities
        fields = '__all__'

class other_service_provisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = other_service_provision
        fields = '__all__'