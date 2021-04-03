from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
from django.core.validators import validate_email


# from libs.helpers import time_it
from .models import Hospital,Specialist,Docter,Appointment
from accounts.users.models import User

class HospitalRequestSerializer(serializers.Serializer):
    """docstring for ClassName"""
    hospital_name = serializers.CharField(required=True)
    email=serializers.EmailField(required=True)
    mobile=serializers.IntegerField(required=True)
    address1=serializers.CharField(required=True)
    address2=serializers.CharField(required=True)
    city=serializers.CharField(required=True)
    pincode=serializers.CharField(required=True)
    state=serializers.CharField(required=True)
    country=serializers.CharField(required=True)

    class Meta:
        model = Hospital
        fields = '__all__'

    def create(self, validated_data):
        hospital = Hospital.objects.create(**validated_data)

        
        return hospital

class hospitalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = '__all__'




class SpecialistRequestSerializer(serializers.Serializer):
    docter_specialization = serializers.CharField(required=True)
    discription = serializers.CharField(required=True)

    class Meta:
        model = Specialist
        fields = '__all__'

    def create(self, validated_data):
        specialist = Specialist.objects.create(**validated_data)

        
        return specialist


class SpecialistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialist
        fields = '__all__'


class DocterRequestSerializer(serializers.ModelSerializer):

    full_name= serializers.CharField(required=True)

    hospital_name = serializers.PrimaryKeyRelatedField(queryset=Hospital.objects.all(),required=True)

    specialization =  serializers.PrimaryKeyRelatedField(queryset=Specialist.objects.all(),required=True)

    email = serializers.CharField(required=True)
    mobile = serializers.CharField(required=True)
    time_zone = serializers.CharField(required=True)
    experiance = serializers.CharField(required=True)
    address1 =serializers.CharField(required=True)
    address2 = serializers.CharField(required=True)
    city=serializers.CharField(required=True)
    pincode=serializers.CharField(required=True)
    state=serializers.CharField(required=True)
    country=serializers.CharField(required=True)

    class Meta:
        model = Docter
        fields = '__all__'


class DocterListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Docter
        fields = '__all__'


class AppointmentRequestSerializer(serializers.Serializer):
    """docstring for ClassName"""
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=True)

    docter =serializers.PrimaryKeyRelatedField(queryset=Docter.objects.all(),required=True)

    appointment_date = serializers.DateField(required=True)

    time_slot = serializers.DateTimeField(required=True)

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        appointment = Appointment.objects.create(**validated_data)

        
        return hospital


class AppointmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'
    