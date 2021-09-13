from django.urls import path, include
from . import views

urlpatterns = [
    path('logup/', views.user_logup),
    path('login/', views.user_login),
    path("logout/", views.logout)
]
