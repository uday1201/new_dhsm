from djongo import models
from django.utils import timezone
# Create your models here.
'''class asha(models.Model):
	asha_id = models.CharField(max_length=10) 
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name'''

class family_profile(models.Model):
	family_id = models.CharField(primary_key=True, max_length=10)
	asha = models.CharField(max_length=50)
	anm = models.CharField(max_length=50)
	health_facility = models.CharField(max_length=100)
	area_code = models.IntegerField()
	area_description = models.TextField()
	date_of_survey = models.DateField(default=timezone.now)
	name_head_of_family = models.CharField(max_length=50)
	address = models.TextField()
	pincode = models.CharField(max_length=6)
	mobile_no = models.CharField(max_length=10)
	landline = models.CharField(max_length=8)
	CATEGORIES = (
		('1', 'General'),
		('2', 'SC'),
		('3', 'ST'),
		('4', 'Other'),
		)
	category = models.CharField(max_length=1, choices=CATEGORIES)
	RELIGION = (
		('1', 'Hindu'),
		('2', 'Muslim'),
		('3', 'Sikh'),
		('4', 'Isai'),
		('5', 'Other'),
		)
	religion = models.CharField(max_length=1, choices=RELIGION)


	def __str__(self):
        	return self.family_id

class basic_amenities(models.Model):
	family_id = models.CharField(primary_key=True, max_length=10)

	TYPE = (
		('1', 'Kaccha'),
		('2', 'Pakka'),
		('3', 'Semi-Pakka'),
		('4', 'Jhuggi'),
		('5', 'Homeless'),
		)
	house_type = models.CharField(max_length=1, choices=TYPE)
	OWNERSHIP = (
		('1', 'rented'),
		('2', 'own'),
		('3', 'government'),
		)
	ownership = models.CharField(max_length=1, choices=OWNERSHIP)
	no_of_rooms = models.IntegerField()
	separate_room = models.BooleanField()
	electricity = models.BooleanField()
	WATER_SOURCE = (
		('1', 'Govt. tap water'),
		('2', 'Hand Pump'),
		('3', 'Tanker'),
		('4', 'Other'),
		)
	water_source = models.CharField(max_length=1, choices=WATER_SOURCE)
	VEHICLE = (
		('1', 'two wheeler'),
		('2', 'three wheeler'),
		('3', 'four wheeler'),
		('4', 'none'),
		)
	vehicle = models.CharField(max_length=1, choices=VEHICLE)
	TOILET = (
		('1', 'own in house'),
		('2', 'public'),
		('3', 'open defacation'),
		)
	toilet_facility = models.CharField(max_length=1, choices=TOILET)
	water_available_in_toilet = models.BooleanField()
	DRAINAGE = (
		('1', 'Closed'),
		('2', 'Open'),
		('3', 'Blocked'),
		)
	drainage = models.CharField(max_length=1, choices=DRAINAGE)
	GARBAGE = (
		('1', 'by sweeper'),
		('2', 'open'),
		('3', 'other'),
		)
	garbage_disposal = models.CharField(max_length=1, choices=GARBAGE)


	def __str__(self):
		return self.family_id

class other_service_provision(models.Model):
	family_id = models.CharField(primary_key=True, max_length=10)
	anganwadi_services = models.BooleanField()
	CATs = models.BooleanField()
	Disability = models.BooleanField()
	PDS = models.BooleanField()


	def __str__(self):
		return self.family_id

'''
class family(models.Model):
	profile = models.EmbeddedModelField(
		model_container = family_profile,
		)

    
    amenities = models.EmbeddedModelField(
    	model_container = basic_amenities,
    	)
    
    
    other = models.EmbeddedModelField(
        model_container=other_service_provision,
    )
	
	family_id = models.CharField(primary_key=True, max_length=10)


    def __str__(self):
    	return self.headline
'''

