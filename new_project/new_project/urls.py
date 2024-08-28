from django.contrib import admin
from django.urls import path, include
from post.api.router import router_post
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion API Blog",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/posts', PostApiView.as_view()),
    path('api/',include(router_post.urls)),

   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
