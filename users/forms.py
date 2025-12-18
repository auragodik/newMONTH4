from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from .models import CustomUser, CERTIFICATE, GENDER, ENGLISH

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    certificate = forms.ChoiceField(choices=CERTIFICATE, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    city = forms.CharField(required=True)
    experience = forms.IntegerField(required=True)
    english_lvl = forms.ChoiceField(choices=ENGLISH, required=True)
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'surname',
            'phone_number',
            'certificate',
            'gender',
            'city',
            'experience',
            'english_lvl',
            'password1',
            'password2',
            'captcha',
        )

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    captcha = CaptchaField()
