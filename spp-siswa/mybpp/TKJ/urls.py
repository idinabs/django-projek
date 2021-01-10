from django.urls import path
from . import views

urlpatterns = [
    path('x', views.X, name='x'),
    path('xi', views.XI, name='xi'),
    path('xii', views.XII, name='xii'),
    # path('xii_absen/', views.XII_ABSEN, name='xii_absen'),
    path('delete_x/<int:delete_x>', views.delete_x, name='delete_x'),
    path('delete_xi/<int:delete_xi>',views.delete_xi, name='delete_xi'),
    path('delete_xii/<int:delete_xii>', views.delete_xii, name='delete_xii'),
    path('update_x/<int:update_x>', views.update_x, name='update_x')
]