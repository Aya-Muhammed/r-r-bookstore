from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='accessories'),
    path('<int:accessory_id>', views.accessory, name='accessory'),
]

