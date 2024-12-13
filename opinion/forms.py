from django import forms
from .models import Opinion
from booking.models import Booking

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['booking', 'rating', 'comment']
        widgets = {
            'booking': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }