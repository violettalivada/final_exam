from django import forms
from django.forms import ModelForm

from webapp.models import Message


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
