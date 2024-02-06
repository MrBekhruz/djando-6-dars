from django import forms
from .models import *

class CompanyForms(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'