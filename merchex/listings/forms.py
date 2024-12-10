from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100, required=False)
    email = forms.EmailField(label="Your email")
    message = forms.CharField(label="Your message", widget=forms.Textarea, max_length=1000)