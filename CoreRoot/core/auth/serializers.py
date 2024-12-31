from dataclasses import field
from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.models import User


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
