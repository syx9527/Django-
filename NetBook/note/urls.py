from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_view),
    path('test_page/', views.test_page),
    path('test_csv/', views.test_csv),
    path('make_page_csv/', views.make_page_csv),
    # path('upload/', views.upload),
]
