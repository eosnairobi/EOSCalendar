from django import forms

from .models import SuggestedEvent


class SuggestedEventForm(forms.ModelForm):
    class Meta:
        model = SuggestedEvent
        fields = '__all__'