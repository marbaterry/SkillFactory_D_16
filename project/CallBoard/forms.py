from django import forms
from .models import *


class ResponseForm(forms.Form):
    take_allow = models.BooleanField(default=False, help_text="Принять предложение")