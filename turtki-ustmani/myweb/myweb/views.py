from django.shortcuts import render, redirect
from app.models import Modelskontak
from app.forms import Formkontak

def load(request):
	posts	= Modelskontak.objects.all()
    
	context = {
		'posts':posts,
	}

	return render(request,'app/load.html',context)


def kontak(request):
    post_form = Formkontak(request.POST or None)

    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
       
            
           
    konteks = {
        'post_form':post_form,
        
        
    } 

    return render(request,'index.html',konteks)