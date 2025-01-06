import re
from django.shortcuts import render

# from CoreRoot.core import post
from core.auth.permissions import UserPermission
from core.models import Comment
from core.comment.serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework import status




class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    # permission_classes = (UserPermission,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()
        post_id = self.kwargs['post_id']
        if post_id is None:
            raise HTTP_404_NOT_FOUND
        queryset = Comment.objects.filter(post__public_id=post_id)
        return queryset
    def get_object(self):
        try:
            obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
            
        except Comment.DoesNotExist:
            raise HTTP_404_NOT_FOUND
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        ## first we need to set the serializer context
        serializer = self.get_serializer(data=request.data)
        ## then we need to check if the serializer is valid
        serializer.is_valid(raise_exception=True)
        ## then we need to create the object
        self.perform_create(serializer)
        ## then we need to return the response
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # def update(self, request, *args, **kwargs):
    #     ## first we need to get the object
    #     instance = self.get_object()
    #     ## then we need to get the serializer
    #     serializer = self.get_serializer(instance, data=request.data)
    #     ## then we need to check if the serializer is valid
    #     serializer.is_valid(raise_exception=True)
    #     ## then we need to perform the update
    #     self.perform_update(serializer)
    #     ## then we need to return the response
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def perform_destroy(self, instance):
    #     instance.delete()
    
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    
    # def perform_update(self, serializer):
    #     serializer.save(edited=True)
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    

    
    # def get_serializer_context(self):
    #     return {'request': self.request}
    
    # def get_serializer_class(self):
    #     return CommentSerializer