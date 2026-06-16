from django.urls import path
from .views import IranTimeview, TargetTimezoneView
from .tasks import simulate_task

urlpatterns = [
    path('irantime/', IranTimeview.as_view(), name='iran-time'),#chack
    path('targettimezone/', TargetTimezoneView.as_view(), name='target-time'),#check
    path('task/', simulate_task, name='simulate-task'),
]

