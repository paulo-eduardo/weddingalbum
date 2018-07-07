from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('pictures.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]
