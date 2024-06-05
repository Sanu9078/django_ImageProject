from django import forms
from app.models import *

class UserModel(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}
        
class ProfileModel(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['username']