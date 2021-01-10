from django.shortcuts import render


def halaman_utama(request):
    return render(request, 'home/data_kehadiran.html')


# TKJ

def absen_x(request):
    return render(request, 'TKJ/kehadiran/x.html')


def absen_xi(request):
    return render(request, 'TKJ/kehadiran/xi.html')


def absen_xii(request):
    return render(request, 'TKJ/kehadiran/xii.html')