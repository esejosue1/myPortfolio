
from django.urls import path
from django.urls import include
from home import views

urlpatterns = [
    path('', views.home, name='home')
    
]