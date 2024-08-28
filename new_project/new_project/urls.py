from django.contrib import admin
from django.urls import path, include
from post.api.router import router_post
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/posts', PostApiView.as_view()),
    path('api/',include(router_post.urls))
]
