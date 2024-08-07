from django.contrib import admin
from django.urls import path
from post.api.views import PostApiView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts', PostApiView.as_view()),
]
