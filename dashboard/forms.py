from django import forms
from . models import User_Details

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = User_Details
        fields =  ['first_name', 'last_name', 'age', 'email','username', 'password']
        widgets = {
            'password': forms.PasswordInput(), 
        }

class loginForms(forms.ModelForm):
    class Meta:
         model = User_Details
         fields =  [ 'username', 'password']
         widgets = {
            'password': forms.PasswordInput(), 
         }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User_Details
        fields = ['first_name', 'last_name', 'age', 'email']

