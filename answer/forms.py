from django import forms
from .models import Answer

class AnswerRegisterForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = (
            'question',
            'answer',
        )

    question = forms.CharField(
        label='質問',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '質問', 'class': 'form-control'})
    )
    answer = forms.CharField(
        label='回答',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '回答', 'class': 'form-control'})
    )

class AnswerUpdateForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = (
            'question',
            'answer',
        )

    question = forms.CharField(
        label='質問',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '質問', 'class': 'form-control'})
    )
    answer = forms.CharField(
        label='回答',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '回答', 'class': 'form-control'})
    )