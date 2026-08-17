from django.urls import path
from .views import IranTimeview, SimulateTaskView, TargetTimezoneView, simulatetaskresultview

urlpatterns = [
    path('irantime/', IranTimeview.as_view(), name='iran-time'),
    path('targettimezone/', TargetTimezoneView.as_view(), name='target-time'),
    path('task/', SimulateTaskView.as_view(), name='simulate-task'),
    path('task-result/<str:task_id>/', simulatetaskresultview.as_view(), name='simulate-task-result')
 ]
