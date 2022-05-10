from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, ),
    path('home', views.home),
    path('delete_employee/<id>', views.delete_employee),
    path('update_employee/<int:id>', views.update_employee)
]