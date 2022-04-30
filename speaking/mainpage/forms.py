import re

from django import forms
from django.core.exceptions import ValidationError

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'country', 'level', 'question', 'connect']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'connect': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Title should not be started with number')
        return title
