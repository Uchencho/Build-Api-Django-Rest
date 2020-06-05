from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Test Project description",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/jwt/', obtain_jwt_token),
    path('api/status/', include('status.api.urls')),
    path('api/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/documentation/second', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
]


# check out this link https://drf-yasg.readthedocs.io/en/stable/readme.html