from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        # fields = ['user', 'first_name', 'last_name']
        exclude = ['user']
