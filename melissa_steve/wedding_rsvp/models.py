from django.db import models

# Create your models here.


class WeddingRSVP(models.Model):
	names = models.CharField(max_length=255)
	attending = models.BooleanField()
	dietary_restrictions = models.CharField(max_length=255)