from django.urls import*
from . import views

urlpatterns = [
    #path('/index/', views.book_service)
    path('index/', views.book_service)
]