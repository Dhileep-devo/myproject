from django.forms import ClearableFileInput
from django import forms
from .models import Feed,FeedFile

...
class FeedModelForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['text']

class FileModelForm(forms.ModelForm):
    class Meta:
        model = FeedFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }