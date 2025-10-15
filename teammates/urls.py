from django.urls import path
from . import views

urlpatterns = [
    path("<int:teammate_id>/", views.TeammateView.as_view()),
    
]