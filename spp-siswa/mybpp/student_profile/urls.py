from django.urls import path
from . import views

urlpatterns = [
    path('HomeData/', views.HomeData, name='HomeData'),
    path('HomeForm/', views.HomeForm, name='HomeForm'),    
    path('delete_data/<int:Delete_Data>', views.Delete_Data, name='Delete'),
    path('update_data/<int:update_data>', views.Update_Data, name='Update'),
    path('delete_Semua', views.delete_semua, name='delete_all'),
]
