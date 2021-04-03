# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.authtoken.models import Token
from libs.models import TimeStampedModel

from model_utils import Choices
from django.db.models import CharField
from .managers import UserManager



class User(TimeStampedModel):
    """
    User model represents the user data in the database.
    """
    STATUS = Choices(
        ('active', 'ACTIVE'),
        ('inactive', 'INACTIVE'),
    )

    GENDER = Choices(
        ('Male','MALE'),
        ('Female','FEMALE'),
        ('Other','OTHER'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    full_name = models.CharField(max_length=64, null=True, blank=False)
    email = models.EmailField(max_length=128, unique=True, db_index=True, blank=False)
    mobile = models.BigIntegerField(
        validators=[
            MinValueValidator(5000000000),
            MaxValueValidator(9999999999),
        ],
        unique=True,
        db_index=True, blank=False)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, null=True, blank=True)


    @property
    def access_token(self):
        token, is_created = Token.objects.get_or_create(user=self)
        return token.key

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']