from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_view),
    path('test_page/', views.add_view),

]
