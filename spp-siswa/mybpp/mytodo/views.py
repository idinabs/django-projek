from django.shortcuts import render
from profile_add.models import Identitas


def home(request):
    postsdata = Identitas.objects.all()
    konteks = {
        'postsdata':postsdata,
        
    }
    return render(request, 'Home.html', konteks)
    

# def jumlah(request):
#     jumlah_data = Identitas.objects.all().count()

#     konteks = {
#         'jumlah_data':jumlah_data
#     }
#     return render(request, 'Home.html', konteks)