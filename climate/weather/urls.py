from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('citylist/', views.citylist, name = 'citylist' ),
]

