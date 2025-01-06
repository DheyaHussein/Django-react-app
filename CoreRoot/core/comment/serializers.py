from pyexpat import model
import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
# from CoreRoot.core import auth
from core.models import Comment, Post, User
from core.post.serializers import PostSerializer
from core.user.serializers import UserSerializer



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='public_id')
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(), slug_field='public_id')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can`t create Comment for author user.")
        return value
    
    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data
        
        return rep
    
    
    class Meta:
        model = Comment
        fields = [
            'id', 'author', 'post', 'body', 'created', 'updated', 'edited'
        ]
        read_only_fields = ['edited']
    