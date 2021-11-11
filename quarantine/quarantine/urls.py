"""quarantine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import settings
from website import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.views.static import serve
from django.conf.urls import url




urlpatterns = [

    path('x', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login, name='login'),
    path('home/', views.home_view, name='home'),
    path('success/', views.success, name='success'),
    path('unsuccessful/', views.unsuccessful, name='unsuccessful'),
    path('success1/', views.success1, name='success1'),
    path('room/success/', views.success1, name='success1'),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/login', views.home_view,name="home"),
    path('host/rooms', views.roomRegistration_view, name='rooms'),
    path('view/mumbai', views.mumbai_view,name='houses'),
    path('view/bangalore', views.bangalore_view,name='houses'),
    path('view/delhi', views.delhi_view,name='houses'),
    path('view/pune', views.pune_view,name='houses'),
    path('dashboard/', views.dashboard_view,name='dashboard'),
    path('room/<int:pk>', views.RoomBookingView.as_view(), name='room-detail'),
    path('test', views.test_view,name='test'),
    path('confirm',views.confirm,name='confirm'),
    path('covidtracker', views.covidView,name='covidtracker'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),



]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
