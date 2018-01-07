from django import forms
from lodge.models.models import Inquiry, Newsletter
from django.core import validators

class InquiryForm(forms.ModelForm):


    class Meta:
        model = Inquiry
        widgets = {
                    'inquirer_first_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'inquirer_last_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'inquiry_title': forms.TextInput(attrs={'class': 'form-control'}),
                    'inquiry_content': forms.TextInput(attrs={'class': 'form-control'}),
                    'inquiry_email_address': forms.EmailInput(attrs={'class': 'form-control'})
                }
        fields = ('inquirer_first_name', 'inquirer_last_name', 'inquiry_title', 'inquiry_content', 'inquiry_email_address')
    
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)
    
    def clean(self):
        print('im cleaning it')
        cleaned_data = super().clean()
        inquiry_email_address = cleaned_data.get("inquiry_email_address")
        # subject = cleaned_data.get("subject")

        if '@' not in inquiry_email_address:
            raise forms.ValidationError(
                "Must use a valid email address"
            )
        return self.cleaned_data


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        widgets = {
                    'subscriber_first_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'subscriber_last_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'subscriber_email_address': forms.EmailInput(attrs={'class': 'form-control'})
                    
                }
        fields = ('subscriber_first_name', 'subscriber_last_name', 'subscriber_email_address')

    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)
        return email
    
    
    def clean(self):
            super().clean()

