from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import MainNews, Language, News, MainNewsEn, MainNewsUz, Timetable, AboutUsRu, AboutUsEn, AboutUsUz

username_validator = UnicodeUsernameValidator()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_('Just Enter the same password, for confirmation'))
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class MainNewsForm(forms.ModelForm):
    class Meta:
        model = MainNews
        fields = ['title', 'image', 'video', 'text', 'date']


class MainNewsFormEn(forms.ModelForm):
    class Meta:
        model = MainNewsEn
        fields = ['title', 'image', 'video', 'text', 'date']


class MainNewsFormUz(forms.ModelForm):
    class Meta:
        model = MainNewsUz
        fields = ['title', 'image', 'video', 'text', 'date']


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']



class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['date', 'time_sunrise', 'time_sunset', 'time_fajr', 
                  'time_satar', 'time_fajr', 'time_zuhr', 'time_asr']
        


class AboutUsRuForm(forms.ModelForm):
    class Meta:
        model = AboutUsRu
        fields = ['title', 'text']


class AboutUsEnForm(forms.ModelForm):
    class Meta:
        model = AboutUsEn
        fields = ['title', 'text']


class AboutUsUzForm(forms.ModelForm):
    class Meta:
        model = AboutUsUz
        fields = ['title', 'text']