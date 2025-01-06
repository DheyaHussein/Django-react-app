from django.urls import path, include
from rest_framework_nested import routers
# from CoreRoot.core import post
from core.user.views import UserViewSet
from core.auth.views import RegisterViewSet, LoginViewSet
from core.post.views import PosrViewSet
from core.comment.views import CommentViewSet


router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'post', PosrViewSet, basename='post')
post_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
## post/post_id/comment this to get the comments of a post
## post/post_id/comment/comment_id this to get a specific comment of a post
## post/post_id/comment/comment_id/comment_id this to get a specific comment of a comment of a post
post_router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = [
    # path('', include('core.user.urls'))
    *router.urls,
    *post_router.urls
    
]
