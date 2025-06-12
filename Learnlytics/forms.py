from django import forms
from .models import InterestType, Course

class UserInputForm(forms.Form):
    interest_choices = [(item, item) for item in InterestType.objects.values_list('interes_name', flat=True).distinct()]
    course_queryset = Course.objects.all()

    interes_name_1 = forms.ChoiceField(
        choices=interest_choices,
        label="Interest Subject",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    interes_name_2 = forms.ChoiceField(
        choices=interest_choices,
        label="Interest Subject",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    last_course_1 = forms.ModelChoiceField(
        queryset=course_queryset,
        label="Last Course",
        empty_label="Choose a course",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    score_last_course_1 = forms.FloatField(
        label="Score for Last Course",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )

    last_course_2 = forms.ModelChoiceField(
        queryset=course_queryset,
        label="Last Course",
        empty_label="Choose a course",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    score_last_course_2 = forms.FloatField(
        label="Score for Last Course",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )

    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')],
        label="Gender",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
