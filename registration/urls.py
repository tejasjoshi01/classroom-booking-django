from django.urls import path , include
from django.views.generic.base import TemplateView
from django.http import request

from . import views



urlpatterns = [
    path('', include('django.contrib.auth.urls')) , 
    path('', TemplateView.as_view(template_name='registration/home.html'), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
