"""
URL configuration for django_chat_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from chat.views import index, login_view, redirect_register, register_view
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', index),
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', redirect_register, name='register'),
    path('login/', login_view, name='login'),
    path('chat/', login_required(TemplateView.as_view(template_name='chat.html')), name='chat'),
]