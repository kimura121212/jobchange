from django import forms
from .models import Interview

class InterviewRegisterForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = (
            'selection_phase',
            'selection_date',
            'question',
            'reflection',
            'other',
        )

    selection_phase = forms.CharField(
        label='選考フェーズ',
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'選考フェーズ', 'class':'form-control'})
    )
    selection_date = forms.DateTimeField(
        label='選考日程',
        required=False,
        widget = forms.DateInput(attrs={"type": "date", 'placeholder': '選考日程', 'class': 'form-control'})
    )
    question = forms.CharField(
        label='質問',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': '質問', 'class': 'form-control'})
    )
    reflection = forms.CharField(
        label='振り返り',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': '振り返り', 'class': 'form-control'})
    )
    other = forms.CharField(
        label='その他',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'その他', 'class': 'form-control'})
    )

class InterviewUpdateForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = (
            'selection_phase',
            'selection_date',
            'question',
            'reflection',
            'other',
        )

    selection_phase = forms.CharField(
        label='選考フェーズ',
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '選考フェーズ', 'class': 'form-control'})
    )
    selection_date = forms.DateTimeField(
        label='選考日程',
        required=False,
        widget = forms.DateInput(attrs={"type": "date", 'placeholder': '選考日程', 'class': 'form-control'})
    )
    question = forms.CharField(
        label='質問',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': '質問', 'class': 'form-control'})
    )
    reflection = forms.CharField(
        label='振り返り',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': '振り返り', 'class': 'form-control'})
    )
    other = forms.CharField(
        label='その他',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'その他', 'class': 'form-control'})
    )