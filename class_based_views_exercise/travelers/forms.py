from django import forms

from travelers.models import Traveler


class TravelerForm(forms.Form):
    class Meta:
        model = Traveler
        exclude = ['registered_at']

        error_messages = {
            "age": {
                "min_value": "Traveler must be at least 18 years old!",
            },
            "email": {
                "invalid": "Provide a valid university email address!",
            }
        }

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'John Doe..'}),
            "email": forms.EmailInput(attrs={'placeholder': 'student@university.com/student@university.net/student@university.org'}),
        }