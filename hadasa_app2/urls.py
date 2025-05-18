from django.urls import*
from . import views

urlpatterns = [
    path('', views.main_fun),
    path('index/', views.main_fun),
    path('api/data/', views.get_comments),
]