from django.shortcuts import render
from profile_add.models import Identitas

def profile(request):
    postsdata = Identitas.objects.all()
    konteks = {
        'postsdata':postsdata
    }
    return render(request, 'profile/profile.html', konteks)