from django import forms
from .models import Sources

class Bulletin_request(forms.ModelForm):
    class Meta:
        model = Sources
        fields = ['link', 'description']