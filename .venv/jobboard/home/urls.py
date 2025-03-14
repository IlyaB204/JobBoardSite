from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('blog/', views.blog_view, name = 'blog'),
    path('candidate/', views.candidate_view, name = 'candidate'),
    path('jobs/', views.jobs_view, name = 'jobs'),
    path('job_detail/', views.job_detail_view, name = 'job_details'),
    path('elements/', views.elevents_view, name = 'elements'),
]