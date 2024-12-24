from django import forms
from .models import iPhone

class iPhoneForm(forms.ModelForm):
    class Meta:
        model = iPhone
        fields = ['color', 'space', 'display']  
