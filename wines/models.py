
from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Red_Wines(models.Model):
    def scale():
        MaxValueValidator(10),
        MinValueValidator(1)
    wine_name = models.CharField(null=True, max_length=50)
    vineyard = models.CharField(null=True, max_length=50)
    region = models.CharField(null=True, max_length=50)
    style = models.CharField(null=True, max_length=50)
    year = models.IntegerField(MaxValueValidator(3000), null=True)
    light_bold = models.IntegerField(scale, null=True)
    sweet_dry = models.IntegerField(scale, null=True)
    smooth_tanic = models.IntegerField(scale, null=True)
    soft_acidic = models.IntegerField(scale, null=True)
    def __str__(self):
        return '%s %s' % (self.wine_name, self.year)
        

class White_Wines(models.Model):
    def scale():
        MaxValueValidator(10),
        MinValueValidator(1)
    wine_name = models.CharField(null=True, max_length=50)
    vineyard = models.CharField(null=True, max_length=50)
    region = models.CharField(null=True, max_length=50)
    style = models.CharField(null=True, max_length=50)
    year = models.IntegerField(MaxValueValidator(3000), null=True)
    light_bold = models.IntegerField(scale, null=True)
    sweet_dry = models.IntegerField(scale, null=True)
    herbaceous_zesty = models.IntegerField(scale, null=True)
    def __str__(self):
        return '%s %s' % (self.wine_name, self.year)