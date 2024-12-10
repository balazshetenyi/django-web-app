from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

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
