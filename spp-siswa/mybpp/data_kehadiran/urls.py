from django.urls import path
from . import views

urlpatterns = [
    path('absen_x/', views.absen_x, name='absen_X'),
    path('absen_xi/', views.absen_xi, name='absen_Xi'),
    path('absen_xii/', views.absen_xii, name='absen_Xii'),
    path('', views.halaman_utama, name='home_kehadiran'),
]