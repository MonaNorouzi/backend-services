from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("timeview/", include("timeviwe.urls")),
    path("admin/", admin.site.urls),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
  
]


