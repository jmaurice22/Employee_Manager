from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee, ),
    path('employee', views.employee )

]