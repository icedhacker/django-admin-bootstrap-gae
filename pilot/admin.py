from django.contrib import admin
from pilot import models


class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortName', 'flagUrl')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('-name',)


class CitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortName', 'countryId')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('-name',)


class TimezoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'utcDiffMinutes', 'countryId')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('-name',)


class VenuesAdmin(admin.ModelAdmin):
    list_display = ('name', 'cityId')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('-name',)


admin.site.register(models.Country, CountriesAdmin)
admin.site.register(models.City, CitiesAdmin)
admin.site.register(models.Timezone, TimezoneAdmin)
admin.site.register(models.Venue, VenuesAdmin)
