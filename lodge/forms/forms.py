from django import forms
from lodge.models.models import Inquiry, Newsletter


class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        widgets = {
                    'inquirer_first_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'inquirer_last_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'inquiry_title': forms.TextInput(attrs={'class': 'form-control'}),
                    'inquiry_content': forms.TextInput(attrs={'class': 'form-control'}),
                    'inquiry_email_address': forms.TextInput(attrs={'class': 'form-control'}),
                    'botcheck' : forms.TextInput(attrs={'class': 'form-control'})
                }
        fields = ('inquirer_first_name', 'inquirer_last_name', 'inquiry_title', 'inquiry_content', 'inquiry_email_address', 'botcheck')

# class NewsLetterForm(forms.ModelForm):

#     class Meta:
#         model = NewsLetter
#         widgets = {
#                     'inquirer_first_name': forms.TextInput(attrs={'class': 'form-control'}),
#                     'inquirer_last_name': forms.TextInput(attrs={'class': 'form-control'}),
#                     'inquiry_title': forms.TextInput(attrs={'class': 'form-control'}),
#                     'inquiry_content': forms.TextInput(attrs={'class': 'form-control'}),
#                     'inquiry_email_address': forms.TextInput(attrs={'class': 'form-control'}),
#                     'botcheck' : forms.TextInput(attrs={'class': 'form-control'})
#                 }
#         fields = ('inquirer_first_name', 'inquirer_last_name', 'inquiry_title', 'inquiry_content', 'inquiry_email_address', 'botcheck')

