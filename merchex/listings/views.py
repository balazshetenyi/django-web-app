from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.models import Band, Listing
from listings.forms import ContactUsForm

def band_list(request):
    bands = Band.objects.all()
    context = {
        'bands': bands
    }
    
    return render(request, 'listings/band_list.html', context)


def band_detail(request, id):
    band = Band.objects.get(id=id)
    context = {
        'band': band
    }
    
    return render(request, 'listings/band_detail.html', context)


def listings(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    
    return render(request, 'listings/listings.html', context)


def contact(request):
    print('The request method is:', request.method)
    print('The POST data is:', request.POST)
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print('The form is valid!')
            print('The cleaned data is:', form.cleaned_data)
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
        else:
            print('The form is invalid!')
    else:
        form = ContactUsForm()
  
    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')