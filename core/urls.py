from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('threats/', views.threats, name='threats'),
    path('safety-tips/', views.tips, name='tips'),
    path('about/', views.about, name='about'),
]
