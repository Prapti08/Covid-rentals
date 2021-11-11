from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
     path('login/', views.login, name='login'),
      path('signup/', views.signup, name='signup'),


]
