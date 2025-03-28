from django import forms
from .models import Sources, Categories, Cat_x_Source

class Bulletin_request(forms.ModelForm):
    class Meta:
        model = Sources
        fields = ['link']

class Cat_request(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['category']

class C_x_S_request(forms.ModelForm):
    class Meta:
        model = Cat_x_Source
        fields = ['source', 'category']
        
