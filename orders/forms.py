from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from orders.models import Users


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    # password = forms.CharField(widget=forms.PasswordInput)
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].login = 'Логин'
    #     self.fields['password'].login = 'Пароль'
    #
    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     if not User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('dsadsad')
    #     user = User.objects.filter(username=username).first()
    #     if user:
    #         if not user.check_password(password):
    #             raise forms.ValidationError("Неверный пароль")
    #     return self.cleaned_data


# class RegisterUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         #fields =['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
#        # widgets = {'FullName': (pattern="^[a-zA-Z]+$" class="form-control" id="validationCustom02" placeholder="Логин")}
#
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             for field in self.fields:
#                 self.fields[field].widget.attrs['class'] = 'form-control'


