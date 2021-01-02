from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('student_profile/', include(('student_profile.urls','student_profile'), namespace='student_profile')),
    path('profile_add/', include(('profile_add.urls','profile_add'), namespace='profile_add')),
]
