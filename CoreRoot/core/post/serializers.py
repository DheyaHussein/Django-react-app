from django.forms import SlugField
from core.models import Post, User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError



class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id',
    read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)    
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='public_id')
    like = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    
    def get_like(self, obj):
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked_post(obj)
    
    def get_likes_count(self, obj):
        return obj.liked_by.count()
    
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can`t create Post for author user.")
        return value
    def update(self, instance, validated_data):
        if not instance.edited:
            # instance.edited = True
            validated_data["edited"] = True
        instance = super().update(instance, validated_data)
        return instance
    
    class Meta:
        model = Post
        fields = [
            'id', 'author', 'body', 'edited', 'created', 'updated',
            'like', 'likes_count']
        read_only_fields = ["edited"]