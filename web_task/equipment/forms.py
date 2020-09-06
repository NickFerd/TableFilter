from django import forms


class DurationFilterForm(forms.Form):
    start_date = forms.CharField(label='Дата начала', required=False)
    stop_date = forms.CharField(label='Дата окончания', required=False)
