from django import forms
from .models import Alert, Profile
from django.contrib.auth.models import User

class AlertForm(forms.ModelForm):
    class Meta:
        model=Alert
        fields=("content","image")
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('photo','hood','contact')
class UserInformation(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name')

    
