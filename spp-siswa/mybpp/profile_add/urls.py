from django.urls import path
from . import views

urlpatterns = [
    path('identitas', views.formpro, name='identitas'),
]