from django import forms
from .models import Car

class CarCreateForm (forms.ModelForm):
    class Meta:
        model=Car
        fields =('make','description', 'model', 'year','price', 'color', 'category' 'image')