from django import forms

from django.forms import widgets


class TaskForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Title')
    status = forms.CharField(max_length=30, required=False, empty_value='Новая')