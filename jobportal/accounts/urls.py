from django.urls import path
from django.urls.resolvers import URLPattern
from .import views


app_name = 'accounts'
urlpatterns = [
     path('login', views.login,name='login'),
     


]
