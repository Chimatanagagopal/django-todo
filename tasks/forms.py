from django import forms
from .models import userRegister
class formRegister(forms.ModelForm):
    class Meta:
        model=userRegister
        fields='__all__'