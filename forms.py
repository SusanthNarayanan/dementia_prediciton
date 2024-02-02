from django import forms
from .models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'sex', 'Age', 'EDUC', 'SES','MMSE','eTIV','nWBV','ASF']
