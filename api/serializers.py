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

class family_membersSerializer(serializers.ModelSerializer):
    class Meta:
        model = family_members
        fields = '__all__'

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = '__all__'
    #family_member_id = serializers.ReadOnlyField()

class rntcpSerializer(serializers.ModelSerializer):
    class Meta:
        model = rntcp
        fields = '__all__'

class ashaSerializer(serializers.ModelSerializer):
    class Meta:
    	model = asha
    	fields = ("name", "dispensary", "anm", "asha_id", "email")
    asha_id = serializers.ReadOnlyField()
