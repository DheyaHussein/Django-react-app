from django.urls import URLPattern, path
from core.user.views import UserViewSet

urlpatterns = [
    path('user/', UserViewSet.as_view({'get': 'list', 'patch': 'update'})),
    
]

