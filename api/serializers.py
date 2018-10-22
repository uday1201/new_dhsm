from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers

class familySerializer(serializers.ModelSerializer):
    class Meta:
        model = family
        fields = '__all__'
