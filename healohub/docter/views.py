# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Hospital,Specialist,Docter,Appointment
from .serializers import DocterRequestSerializer, DocterListSerializer,HospitalRequestSerializer,hospitalListSerializer,SpecialistRequestSerializer,SpecialistSerializer,AppointmentRequestSerializer,AppointmentListSerializer

# Create your views here.
class docterViewSet(GenericViewSet):
	"""
	docter class
	"""
	queryset = Docter.objects.all()
	filter_backends = (filters.OrderingFilter,)
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']

	serializers_dict = {
		'add_docter': DocterRequestSerializer,
		'docter_list': DocterListSerializer,

	}

	def get_queryset(self, filterdata=None):
		if filterdata:
			self.queryset = User.objects.filter(**filterdata)
		return self.queryset
	

	@action(methods=['post'], detail=False, permission_classes=[])
	def add_docter(self, request):
		"""
		Returns docter Registration
		"""
		serializer = self.get_serializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors)

		user = serializer.create(serializer.validated_data)
		if user:
				return Response({"status":"Successfully Registered"})
		return Response({"status": "Not Found"})


	def query_string(self, filterdata):

		dictionary = {}
   
		if "full_name" in filterdata:
			dictionary["full_name__icontains"] = filterdata.pop('full_name')

		if "hospital_name" in filterdata:
			hospital_name = filterdata['hospital_name'].split(',')
			dictionary["hospital_name__in"] = hospital_name

		if "specialization" in filterdata:
			dictionary["specialization__icontains"] = filterdata.pop('specialization')

		
			
		return dictionary



	@action(
		methods=['get'],
		detail=False,
		permission_classes=[],
	)
	def docter_list(self, request, **dict):
		"""
		Return docter list data and groups
		"""
		data = self.get_serializer(self.get_queryset(), many=True).data
		return Response(data, status.HTTP_200_OK)




class HospitalViewSet(GenericViewSet):
	"""
	docter class
	"""
	queryset = Hospital.objects.all()
	filter_backends = (filters.OrderingFilter,)
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']

	serializers_dict = {
		'add_hospital': HospitalRequestSerializer,
		'hospital_list': hospitalListSerializer,

	}

	def get_queryset(self, filterdata=None):
		if filterdata:
			self.queryset = User.objects.filter(**filterdata)
		return self.queryset
	

	@action(methods=['post'], detail=False, permission_classes=[])
	def add_hospital(self, request):
		"""
		Returns docter Registration
		"""
		serializer = self.get_serializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors)

		user = serializer.create(serializer.validated_data)
		if user:
				return Response({"status":"Successfully Registered"})
		return Response({"status": "Not Found"})




	@action(
		methods=['get'],
		detail=False,
		permission_classes=[],
	)
	def hospital_list(self, request, **dict):
		"""
		Return docter list data and groups
		"""
		data = self.get_serializer(self.get_queryset(), many=True).data
		return Response(data, status.HTTP_200_OK)




class SpecialistViewSet(GenericViewSet):
	"""
	docter class
	"""
	queryset = Specialist.objects.all()
	filter_backends = (filters.OrderingFilter,)
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']

	serializers_dict = {
		'add_specialist': SpecialistRequestSerializer,
		'specialist_list': SpecialistSerializer,

	}

	def get_queryset(self, filterdata=None):
		if filterdata:
			self.queryset = User.objects.filter(**filterdata)
		return self.queryset
	

	@action(methods=['post'], detail=False, permission_classes=[])
	def add_specialist(self, request):
		"""
		Returns docter Registration
		"""
		serializer = self.get_serializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors)

		user = serializer.create(serializer.validated_data)
		if user:
				return Response({"status":"Successfully Registered"})
		return Response({"status": "Not Found"})




	@action(
		methods=['get'],
		detail=False,
		permission_classes=[],
	)
	def specialist_list(self, request, **dict):
		"""
		Return docter list data and groups
		"""
		data = self.get_serializer(self.get_queryset(), many=True).data
		return Response(data, status.HTTP_200_OK)




class AppointmentViewSet(GenericViewSet):
	"""
	docter class
	"""
	queryset = Appointment.objects.all()
	filter_backends = (filters.OrderingFilter,)
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']

	serializers_dict = {
		'add_appointment': AppointmentRequestSerializer,
		'appointment_list': AppointmentListSerializer,

	}

	def get_queryset(self, filterdata=None):
		if filterdata:
			self.queryset = User.objects.filter(**filterdata)
		return self.queryset
	

	@action(methods=['post'], detail=False, permission_classes=[])
	def add_appointment(self, request):
		"""
		Returns docter Registration
		"""
		serializer = self.get_serializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors)

		user = serializer.create(serializer.validated_data)
		if user:
				return Response({"status":"Successfully Registered"})
		return Response({"status": "Not Found"})

	@action(
		methods=['get'],
		detail=False,
		permission_classes=[],
	)
	def appointment_list(self, request, **dict):
		"""
		Return docter list data and groups
		"""
		data = self.get_serializer(self.get_queryset(), many=True).data
		return Response(data, status.HTTP_200_OK)
