from django.urls import path
from . import views, home

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', home.index, name='home'),  # Added home URL
    path('register/', views.register, name='register'),  # Added register URL
]
