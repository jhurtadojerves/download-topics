"""Form file"""
# Django
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.forms import forms
from django.forms import CharField, IntegerField
from django.forms.widgets import URLInput


class DownloadForm(forms.Form):
    url = CharField(widget=URLInput, label="Link del topic")
    initial_page = IntegerField(initial=1, label="Página inicial", min_value=1)
    end_page = IntegerField(initial=1, label="Página final", min_value=1)

    def clean(self):
        clean_data = self.cleaned_data
        initial_page = clean_data["initial_page"]
        end_page = clean_data["end_page"]
        if not end_page >= initial_page:
            raise ValidationError(
                "La página final debe ser mayor o igual a la página inicial"
            )
        return clean_data
