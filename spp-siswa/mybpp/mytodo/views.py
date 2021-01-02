from django.shortcuts import render
from profile_add.models import Identitas

def home(request):
    postsdata = Identitas.objects.all()
    konteks = {
        'postsdata':postsdata
    }
    return render(request, 'Home.html', konteks)