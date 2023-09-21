"""phishing URL Configuration

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

from User_Info.views import click_rate, outlook_email, outlook, tengxun_email, tengxun, qiye_email, qiye_result, qiye

urlpatterns = [
    path('admin8888888888/', admin.site.urls),
    path('click_rate', click_rate),
    path('outlook_email', outlook_email),
    path('outlook', outlook),
    path('tengxun_email', tengxun_email),
    path('tengxun', tengxun),
    path('qiye', qiye),
    path('qiye_email', qiye_email),
    path('qiye_result', qiye_result)
]
