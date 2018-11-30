"""dhsm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register(r'family_profile', views.family_profileViewSet)
router.register(r'basic_amenities', views.basic_amenitiesViewSet)
router.register(r'other_service_provision', views.other_service_provisionViewSet)
router.register(r'family_members', views.family_membersViewSet)
router.register(r'member', views.memberViewSet)
router.register(r'rntcp', views.rntcpViewSet)
router.register(r'asha', views.ashaViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
