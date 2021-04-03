from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import UserLoginRequestSerializer, UserRegSerializer
from .models import User

from libs.constants import BAD_REQUEST, BAD_ACTION
from libs.exceptions import ParseException


class UserViewSet(GenericViewSet):
	"""
	user class
	"""
	queryset = User.objects.all().order_by('-created_at')

	filter_backends = (filters.OrderingFilter,)
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']

	serializers_dict = {
		'login': UserLoginRequestSerializer,
		'register': UserRegSerializer,

	}

	def get_queryset(self, filterdata=None):
		print(filterdata)
		if filterdata:
			self.queryset = User.objects.filter(**filterdata)
		return self.queryset

	def get_serializer_class(self):
		"""
		Returns serializer class
		"""
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise ParseException(BAD_ACTION, errors=key)



	@action(methods=['post'], detail=False, permission_classes=[])
	def register(self, request):
		"""
		Returns user Registration
		"""
		user = request.data.copy()
		password = User.objects.make_random_password(length=8,allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789')
		print(password)
		user["password"] = password
		serializer = self.get_serializer(data=user)
		# print(serializer)
		if not serializer.is_valid():
			print(serializer.errors)
			return Response(serializer.errors)

		user = serializer.create(serializer.validated_data)
		print(user)
		if user:
				return Response({"status":"Successfully Registered"}, status=status.HTTP_201_CREATED)
		return Response({"status": "Not Found"}, status.HTTP_404_NOT_FOUND)




	@action(methods=['post'], detail=False, permission_classes=[])
	def login(self, request):
		"""
		Return user login
		"""
		serializer = self.get_serializer(data=request.data)

		if not serializer.is_valid():
			raise ParseException(BAD_REQUEST, serializer.errors)

		user = authenticate(
			email=serializer.validated_data["email"],
			password=serializer.validated_data["password"])

		if not user:
			return Response({'status': 'Invalid Credentials'},
							status=status.HTTP_404_NOT_FOUND)
		token = user.access_token
		name = user.first_name
		id = user.id
		return Response({'token': token, "name": name, 'user_id': id},
						status=status.HTTP_200_OK)

	# @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated, ])
	# def logout(self, request):
	#   """
	#   Return user logout
	#   """
	#   request.user.auth_token.delete()
	#   return Response(status=status.HTTP_200_OK)
