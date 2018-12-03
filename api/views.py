from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics



class family_profileViewSet(viewsets.ModelViewSet):
	queryset = family_profile.objects.all().order_by('-family_id')
	serializer_class = family_profileSerializer

class basic_amenitiesViewSet(viewsets.ModelViewSet):
	queryset = basic_amenities.objects.all().order_by('-family_id')
	serializer_class = basic_amenitiesSerializer

class other_service_provisionViewSet(viewsets.ModelViewSet):
	queryset = other_service_provision.objects.all().order_by('-family_id')
	serializer_class = other_service_provisionSerializer

class family_membersViewSet(viewsets.ModelViewSet):
	queryset = family_members.objects.all().order_by('-family_id')
	serializer_class = family_membersSerializer

'''class TaskFilter(django_filters.FilterSet):
	family_id = django_filters.CharFilter(field_name='family_id')
	family_member_id = django_filters.CharFilter(field_name='family_member_id')

	class Meta:
		model = member
		fields = {
			'family_id',
			'family_member_id'
		}'''


class memberViewSet(viewsets.ModelViewSet):
	queryset = member.objects.all().order_by('-family_member_id')
	serializer_class = memberSerializer
	filter_fields = ('family_id', 'family_member_id')

	#filter_class = TaskFilter


class rntcpViewSet(viewsets.ModelViewSet):
	queryset = rntcp.objects.all().order_by('-family_member_id')
	serializer_class = rntcpSerializer


class ashaViewSet(viewsets.ModelViewSet):
	queryset = asha.objects.all().order_by('-email')
	serializer_class = ashaSerializer