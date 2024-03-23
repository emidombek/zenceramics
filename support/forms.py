from django import forms
from django.core.exceptions import ValidationError
from .models import Contact
from django.core.validators import MaxLengthValidator
class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, validators=[MaxLengthValidator(500)])
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise ValidationError("Your name must be at least 2 characters long.")
        return name