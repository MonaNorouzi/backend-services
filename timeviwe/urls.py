from django.urls import path
from . import apis

urlpatterns = [
    path("iran-time/", apis.IranTimeView.as_view(), name="IR"),
    path("country-time/", apis.CountryTimeView.as_view(), name="country-time"),
    path("signup/", apis.RegisterView.as_view(), name="signup"),
    path("signin/", apis.LoginView.as_view(), name="signin"),
    path("editprof/", apis.EditProfileView.as_view(), name="editprof"),
]