from django import forms
from django.forms import widgets

from webapp.models import Status, ToDo, Type


class ToDoListForm(forms.Form):
    summary = forms.CharField(max_length=200, label='Title', required=True)
    description = forms.CharField(max_length=3000, label='Text', required=False, widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Status', empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Type', empty_label=None)


class StatusForm(forms.Form):
    name = forms.CharField(max_length=20, label='Status', required=True)


class TypeForm(forms.Form):
    name = forms.CharField(max_length=20, label='Status', required=True)

