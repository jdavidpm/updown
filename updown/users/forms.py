from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'user@server.com', 'autocomplete': 'off'}))
    class meta:
        model = User
        fields = ('username', 'email')
    field_order = ('username', 'email')
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'email')
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
    
    def save(self, commit=True):
        profile = super(ProfileUpdateForm, self).save(commit=False)
        profile.image = self.cleaned_data["image"]
        if commit:
            profile.save()
        return profile