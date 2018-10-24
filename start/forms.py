from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationForm(forms.ModelForm):

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.data.get('password2')
        if password != password2:
                raise forms.ValidationError("(100)")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')



