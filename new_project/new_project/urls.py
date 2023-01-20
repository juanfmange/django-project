from django.contrib import admin
from django.urls import path
from post.views import HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', HelloWorld.as_view()),
]
