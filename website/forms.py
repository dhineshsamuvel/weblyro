from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'company', 'service', 'message']

    # Custom validation for phone number format
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Add custom phone number validation logic here if needed
        if phone:
            # Example: Validate phone format (you can adjust this based on your needs)
            if not phone.isdigit():
                raise forms.ValidationError("Phone number must contain only digits.")
            if len(phone) < 10:
                raise forms.ValidationError("Phone number must be at least 10 digits.")
        return phone
