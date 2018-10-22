from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *

class familyViewSet(viewsets.ModelViewSet):
	queryset = family.objects.all().order_by('-family_id')
	serializer_class = familySerializer