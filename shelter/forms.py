from django.forms import TextInput, ModelForm
from django import forms
from .models import Pet


class PetForm(ModelForm):
    date_of_entry = forms.DateField()

    class Meta:
        model = Pet
        fields = '__all__'
