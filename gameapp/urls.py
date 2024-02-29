from django.urls import path
from . import views

urlpatterns = [
    path('', views.gameapp, name='gameapp'),
]