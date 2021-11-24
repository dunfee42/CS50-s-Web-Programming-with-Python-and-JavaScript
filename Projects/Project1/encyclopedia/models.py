from django.db import models
from django import forms

# Create your models here.
class wikiCreation(forms.Form):
    wiki_title = forms.CharField(label="New Wiki", max_length=100)
    wiki_body = forms.CharField(max_length=100, label="Wiki body", widget=forms.Textarea)