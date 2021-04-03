from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
from django.core.validators import validate_email


# from libs.helpers import time_it
from .models import User



class UserLoginRequestSerializer(serializers.ModelSerializer):
    """
    UserLoginSerializer
    """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'access_token')




class UserRegSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=False, min_length=5)
    full_name = serializers.CharField(required=True, min_length=2)
    mobile = serializers.IntegerField(
        required=True,
        min_value=5000000000,
        max_value=9999999999
    )
    dob = serializers.DateField(input_formats=['%d-%m-%Y', ], required=False)
    gender = serializers.CharField(required=False)
    address = serializers.CharField(required=False, )
    


    class Meta:
        model = User

        fields = ('id', 'email','full_name','mobile',
                  'dob', 'gender', 'address')
        write_only_fields = ('password',)
        # read_only_fields = ('id',)

    # @time_it
    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user