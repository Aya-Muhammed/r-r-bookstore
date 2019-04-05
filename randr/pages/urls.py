from django.urls import path
from . import views

urlpatterns = [
    path('', views.preindex, name='preindex'),
    path('home/', views.index, name='index'),
]
