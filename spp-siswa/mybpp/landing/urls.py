from django.urls import path
from . import views

urlpatterns = [
    path('landing', views.landing_home, name='landing' )
]