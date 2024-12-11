from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm

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


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            band = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
                'listings/band_create.html',
                {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect("band-detail", band.id)
    else:
        form = BandForm(instance=band)
        
    return render(request, 'listings/band_update.html', {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    
    if request.method == 'POST':
        band.delete()
        return redirect("band-list")
    
    print("here")
    return render(request, 'listings/band_delete.html', {'band': band})


def listings(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    
    return render(request, 'listings/listings.html', context)


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # create a new `Listing` and save it to the db
            listing = form.save()
            # redirect to the detail page of the listing we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('listings')
    else:
        form = ListingForm()
    
    return render(request, 'listings/listing_create.html', {'form': form})


def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listings")
    else:
        form = ListingForm(instance=listing)
        
    return render(request, 'listings/listing_update.html', {'form': form})


def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    
    if request.method == 'POST':
        listing.delete()
        return redirect("listings")
    
    return render(request, 'listings/listing_delete.html', {'listing': listing})


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