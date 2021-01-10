from django.shortcuts import render, redirect
from profile_add.models import Identitas
from profile_add.forms import Profileform

def X(request):
    kelas_x = Identitas.objects.filter(tingkat_kelas='X')
    
    konteks = {
        'kelas_x':kelas_x
    }
    return render(request, 'TKJ/x.html',konteks)

def delete_x(request, delete_x):
    x = Identitas.objects.filter(id=delete_id)
    x.delete()
    
    return redirect('TKJ:x')

def delete_xi(request, delete_xi):
    xi = Identitas.objects.filter(id=delete_xi)
    xi.delete()

    return redirect('TKJ:xi')

def delete_xii(request, delete_xii):
    xii = Identitas.objects.filter(id=delete_xii)
    xii.delete()

    return redirect('TKJ:xii')

def update_x(request, update_x):
    update_x = Identitas.objects.get(id=update_x)

    data = {
        'nama':update_x.nama,
        'kelas':update_x.kelas,
        'tingkat_kelas':update_x.tingkat_kelas,
        'status_siswa':update_x.status_siswa,
    }

    updateform_x = Profileform(request.POST or None, initial=data, instance=update_x)

    if request.method == 'POST':
        if updateform_x.is_valid():
            updateform_x.save()

            return redirect('TKJ:x')

    konteks = {
        'updateform_x':updateform_x
    }

    return render(request, 'TKJ/update/x.html', konteks)


def XI(request):
    kelas_xi = Identitas.objects.filter(tingkat_kelas='XI')
    
    konteks = {
        'kelas_xi':kelas_xi
    }
    return render(request, 'TKJ/xi.html',konteks)


def XII(request):
    kelas_xii = Identitas.objects.filter(tingkat_kelas='XII')
    
    konteks = {
        'kelas_xii':kelas_xii
    }
    return render(request, 'TKJ/xii.html',konteks)
