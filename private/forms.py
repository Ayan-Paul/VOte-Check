from django.forms import ModelForm
from django import forms
from . models import NewRegister

class NewRegisterForm(forms.ModelForm):
    class Meta:
        model = NewRegister
        fields = ['fullname', 'voterid']
        