from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('register/', views.register_view, name = 'register'),
]