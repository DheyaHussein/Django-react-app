from django.urls import path, include
from rest_framework import routers
from core.user.views import UserViewSet
from core.auth.views import RegisterViewSet, LoginViewSet
from core.post.views import PosrViewSet


router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'post', PosrViewSet, basename='post')

urlpatterns = [
    # path('', include('core.user.urls'))
    *router.urls,
    
]
