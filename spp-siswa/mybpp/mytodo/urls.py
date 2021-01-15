from django.contrib import admin
from django.urls import path, include
from .views import home, LoginView, landing, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', landing, name='landing'),
    path('student_profile/', include(('student_profile.urls','student_profile'), namespace='student_profile')),
    path('profile_add/', include(('profile_add.urls','profile_add'), namespace='profile_add')),
    path('TKJ/', include(('TKJ.urls','TKJ'), namespace='TKJ')),
    path('data_kehadiran/', include(('data_kehadiran.urls','data_kehadiran'), namespace='data_kehadiran')),
    # path('landing/', include(('landing.urls','data_kehadiran'), namespace='landing')),
    path('login/', LoginView, name='login'),
    path("logout/", LogoutView, name='logout'),
]
