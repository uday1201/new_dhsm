from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *

class family_profileViewSet(viewsets.ModelViewSet):
	queryset = family_profile.objects.all().order_by('-family_id')
	serializer_class = family_profileSerializer

class basic_amenitiesViewSet(viewsets.ModelViewSet):
	queryset = basic_amenities.objects.all().order_by('-family_id')
	serializer_class = basic_amenitiesSerializer

class other_service_provisionViewSet(viewsets.ModelViewSet):
	queryset = other_service_provision.objects.all().order_by('-family_id')
	serializer_class = other_service_provisionSerializer