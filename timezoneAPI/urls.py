from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('timeviwe.urls'))
]


