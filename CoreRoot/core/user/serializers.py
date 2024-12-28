from rest_framework import serializers
from core.models import User



class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', 
                               read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "email",
            "is_active",
            "created",
            "updated",
            "posts_count",
        ]
        read_only_field = ['is_active']        