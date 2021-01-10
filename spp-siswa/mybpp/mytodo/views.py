from django.shortcuts import render, redirect
from profile_add.models import Identitas
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    postsdata = Identitas.objects.all()
    konteks = {
        'postsdata':postsdata,
        
    }
    return render(request, 'Home.html', konteks)

def landing(request):
    return render(request, 'landing/index.html')

def LoginView(request):
    if request.method == 'POST':

        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password=password_login)
        
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return redirect('login')

    return render(request, 'user/login.html')

# def LogoutView(request):
#     if request.method == 'POST':
#         if request.POST["logout"] == "Submit":
#             logout(request)


#     return render(request, 'user/logout.html')
