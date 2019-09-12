from django import forms
from .models import Company

class CompanyRegisterForm(forms.Form):
    company_name = forms.CharField(
        label='企業名',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'企業名', 'class':'form-control'})
    )

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name',)

    company_name = forms.CharField(
        label='企業名',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'企業名', 'class':'form-control'})
    )