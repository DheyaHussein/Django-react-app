from tkinter import N
import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.forms import CharField
from django.http import Http404
# Create your models here.


class UserManager(BaseUserManager):
    def get_object_by_public_id(self, pulic_id):
        try:
            instance = self.get(pulic_id=pulic_id)
            return instance
        except(ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        
    def create_user(self, username, email, password=None, **kwargs):
        """
            create and reutrn  a User with username , email , phone number, password
        """
        if username is None:
            raise TypeError('User must have an username')
        elif email is None:
            raise TypeError('User must have an email')
        elif password is None:
            raise TypeError('User must have an password')
        
        user = self.model(username=username,
                          email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password=None, **kwargs):
        """
            create and reutrn  a User with superuser (admin) permissions
        """
        if username is None:
            raise TypeError('User must have an username')
        elif email is None:
            raise TypeError('User must have an email')
        elif password is None:
            raise TypeError('User must have an password')
        
        user = self.model(username=username,
                          email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
        
        
        
            
            
            
            



class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, 
                                 default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True,
                                 max_length=255, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    
        



