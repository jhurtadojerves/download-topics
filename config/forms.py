"""Form file"""
# Django
from django.forms import forms
from django.forms import CharField, IntegerField
from django.forms.widgets import URLInput


class DownloadForm(forms.Form):
    url = CharField(widget=URLInput)
    pages = IntegerField()
