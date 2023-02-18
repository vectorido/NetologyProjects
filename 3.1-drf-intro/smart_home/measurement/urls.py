from django.urls import path

from .views import SensorView, MeasurementList, SensorList

urlpatterns = [
    path('measurements/', MeasurementList.as_view()),
    path('sensors/', SensorList.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
]
