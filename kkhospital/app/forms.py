from django import forms
from allauth.account.forms import LoginForm
from django.utils.translation import ugettext_lazy as _

# class Login_Mod(LoginForm):
#     def __init__(self, *args, **kwargs):
#         super(Login_Mod, self).__init__(*args, **kwargs)
#         # self.fields['login'].label = 'Username'
#         self.fields['login'].widget = forms.TextInput(
#             attrs={
#                 'type': 'email', 
#                 'class': 'form-control input-username'
#             })
#         self.fields['password'].widget = forms.PasswordInput(
#             attrs={
#                 'class': 'form-control input-password'
#             })
