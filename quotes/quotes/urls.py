"""quotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from quotes_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage),
    path('newUser',views.newUser),
    path('login',views.login),
    path('home',views.home),
    path('Success',views.Success),
    path('edit/<quoteid>',views.edit),
    path('stats/<userid>',views.stats),
    path('logout',views.logout),
    path('makequote',views.makequote),
    path('editquote/<quoteid>',views.editquote),
    path('boop/<quoteid>',views.boop),
    path('addfavorite/<quoteid>',views.addfavorite),
]
