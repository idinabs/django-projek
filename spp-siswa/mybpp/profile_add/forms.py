from django import forms
from . models import Identitas

class Profileform(forms.ModelForm):
    class Meta:
        model = Identitas
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput(
                attrs= {
                    'class':'form-control',
                }
            ),
           'kelas' : forms.Select(
                attrs= {
                    'class':'form-control',
                }
            ),
           'nis_siswa' : forms.TextInput(
                attrs= {
                    'class':'form-control',
                }
            ),
           'tingkat_kelas' : forms.Select(
                attrs= {
                    'class':'form-control',
                }
            )
        }
        