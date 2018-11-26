from django import forms
from .models import These, ThesisEntries
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
            raise forms.ValidationError("(100)")
        return email

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class ThesisForm(forms.ModelForm):

    def clean_thesenArgument(self):
        thesenArgument = self.cleaned_data.get('thesenArgument')
        if len(thesenArgument) < 150:
            raise forms.ValidationError("(100)")
        return thesenArgument

    def clean_thesenFazit(self):
        thesenFazit = self.cleaned_data.get('thesenFazit')
        if len(thesenFazit) < 30:
            raise forms.ValidationError("(100)")
        return thesenFazit

    class Meta:
        model = These
        fields = ('thesenTitel', 'thesenArgument', 'thesenFazit', 'thesenQuelle')


class ThesisEntryForm(forms.ModelForm):

    def clean_thesisEntriesArgument(self):
        thesisEntriesArgument = self.cleaned_data.get('thesisEntriesArgument')
        if len(thesisEntriesArgument) < 150:
            raise forms.ValidationError("(100)")
        return thesisEntriesArgument

    def clean_thesisEntriesFazit(self):
        thesisEntriesFazit = self.cleaned_data.get('thesisEntriesFazit')
        if len(thesisEntriesFazit) < 30:
            raise forms.ValidationError("(100)")
        return thesisEntriesFazit

    class Meta:
        model = ThesisEntries
        fields = ('thesisEntriesTitel', 'thesisEntriesArgument', 'thesisEntriesFazit', 'thesisEntriesQuelle')
