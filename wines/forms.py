from django import forms
from .models import Wine

# Added comments
class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ('wine_name', 'price', 'varietal', 'description')