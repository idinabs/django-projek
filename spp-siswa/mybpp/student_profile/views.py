from django.shortcuts import render, redirect
from profile_add.models import Identitas
from profile_add.forms import Profileform
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def HomeData(request):
    postsdat = Identitas.objects.all()
    konteks = {
        'postsdat':postsdat,
        }
    return render(request, 'profile/profile.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def Delete_Data(request, Delete_Data):
    delete_data = Identitas.objects.get(id=Delete_Data)
    delete_data.delete()

    return redirect('student_profile:HomeData')

@login_required(login_url=settings.LOGIN_URL)
def delete_semua(request):
    delete_semua = Identitas.objects.all()
    delete_semua.delete()

    return redirect('home')

@login_required(login_url=settings.LOGIN_URL)
def Update_Data(request, update_data):
    update_data = Identitas.objects.get(id=update_data)

    data = {
        'nama':update_data.nama,
        'kelas':update_data.kelas,
        'tingkat_kelas':update_data.tingkat_kelas,
        'status_siswa':update_data.status_siswa,
    }

    updateform_data = Profileform(request.POST or None, initial=data, instance=update_data)

    if request.method == 'POST':
        if updateform_data.is_valid():
            updateform_data.save()

            return redirect('student_profile:HomeData')

    konteks = {
        'updateform_data':updateform_data
    }

    return render(request, 'profile/update/update.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def HomeForm(request):
    postform = Profileform(request.POST)
    if request.method == "POST":
        if postform.is_valid():
            postform.save()

            return redirect('student_profile:profile')
    
    konteks = {
        'postform':postform,
    }

    return render(request, 'add/add.html', konteks)
