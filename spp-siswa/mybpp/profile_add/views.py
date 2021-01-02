from django.shortcuts import render, redirect
from . models import Identitas
from . forms import Profileform

def profile(request):
    postpro = Identitas.objects.all()
    konteks = {
        'postpro':postpro
    }
    return render(request, 'add/add.html', konteks)

def formpro(request):
    postform = Profileform(request.POST)
    if request.method == "POST":
        if postform.is_valid():
            postform.save()

            return redirect('student_profile:profile')
    
    konteks = {
        'postform':postform
    }

    return render(request, 'add/add.html', konteks)