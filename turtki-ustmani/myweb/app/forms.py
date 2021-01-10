from django import forms
from . models import Modelskontak

class Formkontak(forms.ModelForm):
    class Meta:
        model = Modelskontak
        fields = [
            'name',
            'coment',
        ]

        widgets = {
            'name':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Masukan nama anda'
                }
            ),
             
          'coment':forms.Textarea(
                attrs = {
                    'class':'form-control',
                     'placeholder':'Masukan pesan anda'
                }
            )
        }
