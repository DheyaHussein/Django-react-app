from django.urls import URLPattern, path
from core.user.views import UserViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
]

