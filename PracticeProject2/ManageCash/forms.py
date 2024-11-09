from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class Auth_form(AuthenticationForm):
    class Meta:
        model=CustomUser
        fields=['username','password']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCash
        fields = ['source', 'datetime', 'amount', 'description']
        widgets={
            'datetime':forms.DateInput(attrs={'type':'date', 'class':'date-field'}),
            }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'datetime']
        widgets={
            'datetime':forms.DateInput(attrs={'type':'date', 'class':'date-field'}),
            }