from django.contrib import admin

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active', 'official_homepage')
    

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'description', 'sold', 'year', 'type')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
