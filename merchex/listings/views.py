from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    context = {
        'bands': bands
    }
    
    return render(request, 'listings/hello.html', context)


def about(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    
    return render(request, 'listings/about.html', context)
