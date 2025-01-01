from urllib import response
from django.shortcuts import render
from core.models import Post
from rest_framework.permissions import IsAuthenticated
from core.post.serializers import Postserializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

class PosrViewSet(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    permission_classes = (IsAuthenticated, )
    serializer_class = Postserializer
    
    def get_object(self):
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])
        
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
