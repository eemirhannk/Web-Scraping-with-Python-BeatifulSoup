from email.policy import default
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Notebook(models.Model):
    marka = models.CharField(max_length=50, null=True, blank=True)
    resim = models.CharField(max_length=20, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    modelNo =  models.CharField(max_length=50, null=True, blank=True)
    isletimSistemi =  models.CharField(max_length=50, null=True, blank=True)
    islemciTipi =  models.CharField(max_length=50, null=True, blank=True)
    islemciNesli = models.CharField(max_length=10, null=True, blank=True)
    ram =  models.CharField(max_length=50, null=True, blank=True)
    diskBoyutu =  models.CharField(max_length=50, null=True, blank=True)
    diskTuru =  models.CharField(max_length=10, null=True, blank=True)
    ekranBoyutu =   models.CharField(max_length=50, null=True, blank=True)
    puan =   models.CharField(max_length=50, null=True, blank=True)
    fiyat =   models.CharField(max_length=50, null=True, blank=True)
    urunLink =  models.CharField(max_length=1000, null=True, blank=True)
    urunSite =  models.CharField(max_length=200, null=True, blank=True)