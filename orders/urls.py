from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderView.as_view()),
    path("create/", views.CreateOrderView.as_view()),
    
]