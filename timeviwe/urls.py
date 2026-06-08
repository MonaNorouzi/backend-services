from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .apis import (IranTimeApi,TargetTimezoneApi,UserRegisterApi,UserProfileUpdateApi)

time_patterns = [
    path('iran/', IranTimeApi.as_view(), name='iran-time'),
    path('target/', TargetTimezoneApi.as_view(), name='target-time'),
]

user_patterns = [
    path('register/', UserRegisterApi.as_view(), name='register'),
    path('profile/update/', UserProfileUpdateApi.as_view(), name='profile-update'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('time/', include((time_patterns, 'time'))),
    path('users/', include((user_patterns, 'users'))),
]