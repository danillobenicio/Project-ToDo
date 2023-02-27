from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
]