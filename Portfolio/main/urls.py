from django.urls import path

from main import views

urlpatterns = [
    path('projects/', views.projects),

    path('', views.index)
]