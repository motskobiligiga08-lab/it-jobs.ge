from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs_list, name='jobs_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('post-job/', views.post_job, name='post_job'),
    path('developers/', views.for_developers, name='for_developers'),
    path('employers/', views.for_employers, name='for_employers'),
    path('about/', views.about, name='about'),
]
