from rest_framework.routers import DefaultRouter
from post.api.views import PostViewSet

router_post = DefaultRouter()

router_post.register('posts', PostViewSet, basename='post')