from math import e
import re
from rest_framework.permissions import BasePermission, SAFE_METHODS



class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        
        elif view.basename == "post":
            return bool(request.user and request.user.is_authenticated)
        elif view.basename == "comment":
            if request.method in ['DELETE']:
                return bool(request.user.is_supsruser or request.user in [obj.author, obj.post.author])
            return bool(request.user and request.user.is_authenticated)
        return False

    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
        #     return True
        # return obj.author == request.user
        if view.basename == ["post", "comment"]:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            return bool(request.user and request.user.is_authenticated)
        return False