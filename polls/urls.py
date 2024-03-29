"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
import polls

app_name = 'polls'

urlpatterns = [
    
    path('index/', views.index, name='index'),
    
    path('person/<int:person_id>/', views.show_specific_person, name='show_specific_person'),
    
    path('todo_list/<int:todo_id>/', views.show_specific_todo_list, name='show_specific_todo_list'),

]
