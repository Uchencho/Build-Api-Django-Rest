from django.contrib import admin
from django.urls import path, include
from .views import MyTokenObtainPairView
# from rest_framework_jwt.views import obtain_jwt_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/p/', include('django.contrib.auth.urls')),
    path('api/auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/status/', include('status.api.urls')),
    path('api/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/documentation/second', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
]


# check out this link https://drf-yasg.readthedocs.io/en/stable/readme.html
# pip install -U drf-yasg
# INSTALLED_APPS = [
#    ...
#    'drf_yasg',
#    ...
# ]
# then the view above