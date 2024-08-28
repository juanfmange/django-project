from rest_framework.routers import DefaultRouter
from post.api.views import PostModelViewSet

router_post = DefaultRouter()

router_post.register('posts', basename='post', viewset=PostModelViewSet)