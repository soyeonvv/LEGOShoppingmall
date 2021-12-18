from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage),
    path('mypage/', views.mypage),
    path('manufacturer/', views.manufacturer)
]