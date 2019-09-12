from django import forms

class CompanyRegisterForm(forms.Form):
    company_name = forms.CharField(
        label='企業名',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'企業名', 'class':'form-control'})
    )