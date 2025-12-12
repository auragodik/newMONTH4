from django import forms
from books.models import CustomUser
from django.contrib.auth.forms import UserCreationForm



# class CustomUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     phone_number = forms.CharField(required=True)
#     first_name = forms.CharField(required=True)
#     surname = forms.CharField(required=True)
#     certificate = forms.ChoiceField(CustomUser.certificate, required=True)
#     gender = forms.ChoiceField(CustomUser.gender, required=True)
#     city = forms.CharField(required=True)
#     experience = forms.IntegerField(required=True)
#     english_lvl = forms.ChoiceField(CustomUser.english_lvl, required=True)


#     class Meta:
#         model = CustomUser
#         fields = (
#             'first_name',
#             'surname',
#             'phone_number',
#             'email'
#         )
