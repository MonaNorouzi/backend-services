from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserProfileUpdateview, UserRegisterview

urlpatterns = [
    path('register/', UserRegisterview.as_view(), name='register'),
    path('profile/update/', UserProfileUpdateview.as_view(), name='profile-update'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
