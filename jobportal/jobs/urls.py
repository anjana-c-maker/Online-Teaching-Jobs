from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.urls import include


app_name = 'jobs'

urlpatterns = [
    path('',views.index,name='index'),
     path('register', views.register,name='register'),
     path('register_jobseeker', views.register_jobseeker,name='reg-job-seeker'),
     path('register_employer', views.register_employer,name='reg-employer'),
   


]
