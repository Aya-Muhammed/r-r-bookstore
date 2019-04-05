from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='books'),
    path('<int:book_id>/', views.book, name='book'),
    path('advanced-search/', views.advanced_search, name='advanced_search'),
    path('advanced-search/result/', views.result, name='result'),
]

