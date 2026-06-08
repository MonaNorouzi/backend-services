from django.urls import path
from . import views

urlpatterns = [
    path("iran-time/", views.IranTimeView.as_view(), name="IR"),
    path("country-time/", views.CountryTimeView.as_view(), name="country-time"),
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path("signin/", views.LoginView.as_view(), name="signin"),
    path("editprof/", views.EditProfileView.as_view(), name="editprof"),
]