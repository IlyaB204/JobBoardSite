from . import views
from django.urls import path


urlpatterns = [
    path('post_vacancy/', views.upload_vacancy_view, name = 'vacancy')
]