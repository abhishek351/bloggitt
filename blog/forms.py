from django import forms
from .models import contact,profile,post
from django.contrib.auth.models import User


class contactform(forms.ModelForm):
       class Meta:
        model = contact
        fields = "__all__"

class blogForm(forms.ModelForm):
       class Meta:
        model = post
        exclude = ('user',)



class UserUpdateform(forms.ModelForm):
       class Meta:
             model=User
             fields=['username','email','first_name','last_name']


  
class ProfileUpdateform(forms.ModelForm):
       class Meta:
             model=profile
             fields=['image']      