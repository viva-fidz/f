from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class MyRegistrationForm(UserCreationForm):
    # image = forms.ImageField(help_text='Загрузить фото')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # image


class UserChangeForm(MyRegistrationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема')
    sender = forms.EmailField(label='Ваш e-mail')
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Сообщение')
    copy = forms.BooleanField(required=False, label='Поставьте галочку, если хотите получить копию письма')
