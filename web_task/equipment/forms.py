from django import forms
from django.core.exceptions import ValidationError
from .models import Client, Mode, Equipment


def get_list(model):
    """Function to retrieve names from Models
    returns a list of tuples"""
    objects = model.objects.all()
    obj_list = []
    for obj in objects:
        obj_list.append((obj.id, obj.name))
    obj_list.append((-100, 'All'))  # -100 is chosen because it is unlikely to be an id in a model
    return obj_list


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            'Input value should be positive',
            params={'value': value}
        )


class DurationFilterForm(forms.Form):
    """Form for filtering the table"""
    client = forms.MultipleChoiceField(choices=get_list(Client), label='Клиенты',
                                       required=False)
    mode = forms.MultipleChoiceField(choices=get_list(Mode), label='Режим работы',
                                     required=False)
    equip = forms.MultipleChoiceField(choices=get_list(Equipment), label='Оборудование',
                                      required=False)
    duration = forms.IntegerField(label='Длительность состояния', required=False,
                                  validators=[validate_positive])
    start_date = forms.DateField(label='Начало (YYYY-MM-DD)', required=False)
    stop_date = forms.DateField(label='Конец (YYYY-MM-DD)', required=False)
    start_hour = forms.TimeField(label='Время начала (%H:%M)', required=False)
    stop_hour = forms.TimeField(label='Время окончания (%H:%M)', required=False)

