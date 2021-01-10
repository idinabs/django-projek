from django.shortcuts import render
from profile_add.models import Identitas



def halaman_utama(request):
    return render(request, 'home/data_kehadiran.html')


# TKJ

def absen_x(request):
    return render(request, 'TKJ/kehadiran/x.html')


def absen_xi(request):
    absen_xi = Identitas.objects.filter(tingkat_kelas='XI')
    
    konteks = {
        'absen_xi':absen_xi
    }
    return render(request, 'TKJ/kehadiran/xi.html',konteks)




def absen_xii(request):
    absen_xii = Identitas.objects.filter(tingkat_kelas='XII')
    
    konteks = {
        'absen_xii':absen_xii
    }
    return render(request, 'TKJ/kehadiran/xii.html',konteks)

