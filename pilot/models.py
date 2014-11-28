from django.forms import ModelForm
from django.db import models

# Create your models here.


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    shortName = models.CharField(max_length=8)
    flagUrl = models.CharField(max_length=250)

    class Meta:
      db_table = 'Countries'
      managed = False

    def __unicode__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=10)
    countryId = models.ForeignKey(Country, db_column='CountryId')

    class Meta:
      db_table = 'Cities'
      managed = False

    def __unicode__(self):
        return self.name


class Timezone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    utcDiffMinutes = models.IntegerField()
    countryId = models.ForeignKey(Country, db_column='CountryId')

    class Meta:
      db_table = 'Timezone'
      managed = False

    def __unicode__(self):
        return self.name


class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cityId = models.ForeignKey(City, db_column='CityId')

    class Meta:
      db_table = 'Venues'
      managed = False

    def __unicode__(self):
        return self.name
