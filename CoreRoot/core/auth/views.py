from tokenize import TokenError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class RegisterViewSet(ViewSet):
    serializer_class = RegisterSerializer
    # permission_classes = (AllowAny)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token), 
        }
        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
            
            
        }, status=status.HTTP_201_CREATED )
        

class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer
    http_method_names = ['post']
    
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            # refresh = RefreshToken.for_user(user)
            
            # res = {
            #     "refresh": str(refresh),
            #     "access": str(refresh.access_token),
            # }
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        except Exception as e :
             return Response({"detail": "An error occurred during login."},
                             status=status.HTTP_400_BAD_REQUEST)
            
    
    