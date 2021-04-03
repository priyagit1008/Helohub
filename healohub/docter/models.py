# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
# from rest_framework.authtoken.models import Token
from libs.models import TimeStampedModel
from accounts.users.models import User
from model_utils import Choices
from django.db.models import CharField

# Create your models here.
class Hospital(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hospital= models.CharField(max_length=64,blank=False)
    email = models.EmailField(max_length=128, unique=True, db_index=True, blank=False)
    mobile = models.BigIntegerField(
	  validators=[
		MinValueValidator(5000000000),
		MaxValueValidator(9999999999),
	  ],
	  unique=True,
	  db_index=True, blank=False)
    address1 = models.CharField(max_length=64, null=True, blank=True)
    address2 = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    pincode=models.CharField(max_length=64, null=True, blank=True)
    state=models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)

    USERNAME_FIELD = 'hospital_name'
    REQUIRED_FIELDS = ['email','mobile']

class Specialist(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    specialization = models.CharField(max_length=64, null=True, blank=False)
    discription = models.CharField(max_length=64, null=True, blank=False)
    
    USERNAME_FIELD = 'docter_specialization'
    REQUIRED_FIELDS = ['discription']


class Docter(AbstractBaseUser, PermissionsMixin,TimeStampedModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  full_name= models.CharField(max_length=64, null=True, blank=False)

  hospital_name = models.ForeignKey(Hospital,
	on_delete=models.PROTECT,
	related_name='hospital_name',null=True,blank=False)

  specialization =  models.ForeignKey(Specialist,
	on_delete=models.PROTECT,
	related_name='docter_specialist',null=True,blank=False)

  email = models.EmailField(max_length=128, unique=True, db_index=True, blank=False)
  mobile = models.BigIntegerField(
	validators=[
	    MinValueValidator(5000000000),
	    MaxValueValidator(9999999999),
	],
	unique=True,
	db_index=True, blank=False)
  time_zone=models.CharField(max_length=64, null=True, blank=True)
  experiance = models.CharField(max_length=64, null=True, blank=True)
  address1 = models.CharField(max_length=64, null=True, blank=True)
  address2 = models.CharField(max_length=64, null=True, blank=True)
  city = models.CharField(max_length=64, null=True, blank=True)
  pincode=models.CharField(max_length=64, null=True, blank=True)
  state=models.CharField(max_length=64, null=True, blank=True)
  country = models.CharField(max_length=64, null=True, blank=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['hospital_name','specialization','mobile']

class Meta:
	app_label = 'docter'
	db_table = 'api_docter'

class Appointment(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user=models.ForeignKey(User,
	on_delete=models.PROTECT,
	related_name='user_name',null=True,blank=False)

    docter = models.ForeignKey(Docter,
	on_delete=models.PROTECT,
	related_name='docter_name',null=True,blank=False)

    appointment_date = models.DateField(blank=True,null=True)
    time_slot = models.DateTimeField(default=0)

class Meta:
	app_label = 'appointment'
	db_table = 'api_appointment'
