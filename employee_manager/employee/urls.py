from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee, ),
    path('employee', views.employee),
    path('employee_registration', views.employee_registration),

]
