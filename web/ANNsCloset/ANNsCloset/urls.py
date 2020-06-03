"""ANNsCloset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import login.views
import step1.urls
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', step1.views.main, name ='main'),
    path('step1/', include(step1.urls), name='step1'),
    path('login',login.views.login,name='login'),
    path('signup/',login.views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),
    path('logout/',login.views.logout, name='logout'),


]
