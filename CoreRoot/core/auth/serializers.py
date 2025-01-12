from dataclasses import field
from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login


class RegisterSerializer(UserSerializer):
    """   Registration serializer for requests and user creation


    Args:
        UserSerializer (_type_): _description_
    """
    # make sure the password is at laest 8 characters long 
    
    password  = serializers.CharField(max_length=128,
                                      min_length=8, write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'password'
        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data =  super().validate(attrs)
        # print(data)
        refresh = self.get_token(self.user)     
        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['accress'] = str(refresh.access_token)
        
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
            
        return data
        