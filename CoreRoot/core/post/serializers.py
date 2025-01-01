from django.forms import SlugField
from core.models import Post, User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError



class Postserializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id',
    read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)    
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='public_id')
    
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can`t create Post for author user.")
        return value
    
    class Meta:
        model = Post
        fields = [
            'id', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields = ["edited"]