from django import forms

from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100, required=False)
    email = forms.EmailField(label="Your email")
    message = forms.CharField(label="Your message", widget=forms.Textarea, max_length=1000)
    

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'