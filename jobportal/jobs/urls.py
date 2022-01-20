from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns = [
    path('',views.index,name='index'),
     path('register', views.register,name="register"),
     path('signin', views.signin,name="signin"),

]