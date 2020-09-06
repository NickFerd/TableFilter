from django import forms


class DurationFilterForm(forms.Form):
    start_date = forms.CharField(label='Начало (YYYY-MM-DD)', required=False)
    stop_date = forms.CharField(label='Конец (YYYY-MM-DD)', required=False)
