from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add/', views.addTask, name='addTask'),
    path('remove/<int:taskId>/', views.removeTask, name='removeTask'),
    path('change/<int:taskId>/', views.changeStatus, name='changeStatus'),
]