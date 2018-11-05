from  django import forms
from .models import StudentProfile


#this is for signup form

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))




class ProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': 'jobaer'}
                                            ))
    email = forms.CharField(widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': 'something@gmail.com'}
                                            ))
    phone = forms.IntegerField(widget=forms.NumberInput(
                                            attrs={'class': 'form-control', 'placeholder': '01...'}
                                            ))

    gender = forms.CharField(widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': 'Describe..'}
                                            ))
    nationality = forms.CharField(widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': 'Describe..'}
    ))
    user = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'jh'}
    ))
    class Meta:
        model = StudentProfile
        fields = {
            'name',
            'email',
            'phone',
            'gender',
            'nationality',
            'user'
        }