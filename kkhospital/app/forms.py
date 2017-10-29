from django import forms
from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm
from django.utils.translation import ugettext_lazy as _

class Login_Mod(LoginForm):
    def __init__(self, *args, **kwargs):
        super(Login_Mod, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['class'] = 'form-control input-username'
        self.fields['password'].widget.attrs['class'] = 'form-control input-password'
        # for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'


class Signup_Mod(SignupForm):
    username = forms.RegexField(
        max_length=30, regex=r"^[\w.@+-]+$",
        help_text=_("จำเป็นต้องกรอก. ไม่เกิน 30 ตัวอักษร ประกอบด้วย พยัญชนะ, ตัวเลข หรือ "
                    "@/./+/-/_ เท่านั้น"),
        error_messages={
            'invalid': _("ชื่อผู้ใช้ ต้องประกอบด้วย พยัญชนะ, ตัวเลข หรือ "
                         "@/./+/-/_ เท่านั้น")},
    )
    email = forms.EmailField(required=True, max_length=100, help_text="kkulsri@kk.com")

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(Signup_Mod, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = 'มากกว่า 8 ตัวขึ้นไป'
        self.fields['password2'].help_text = 'ต้องตรงกับช่องใส่รหัสผ่าน'


# class PasswordChange_Mod(ChangePasswordForm):
#     def __init__(self, *args, **kwargs):
#         super(PasswordChange_Mod, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control input-password'
