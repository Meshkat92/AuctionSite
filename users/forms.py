from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email']
    
    
            
        

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        if commit:
            user.save()

        return user
        
    
    
