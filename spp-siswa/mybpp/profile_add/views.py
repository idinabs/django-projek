from django.shortcuts import render, redirect
from . models import Identitas
from . forms import Profileform
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def profile(request):
    postpro = Identitas.objects.all()
    konteks = {
        'postpro':postpro
    }
    return render(request, 'add/add.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def formpro(request):
    postform = Profileform(request.POST)
    if request.method == "POST":
        if postform.is_valid():
            postform.save()

            return redirect('student_profile:HomeData')
    
    konteks = {
        'postform':postform
    }

    return render(request, 'add/add.html', konteks)