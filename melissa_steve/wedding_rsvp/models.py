from django.db import models

# Create your models here.


class WeddingRSVP(models.Model):
    names = models.CharField(max_length=255)
    attending = models.BooleanField()
    dietary_restrictions = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.names

    @classmethod
    def create(cls, attending, names, dietary_restrictions):
        weddingRSVP = cls(attending=attending, names=names, dietary_restrictions=dietary_restrictions)
        return weddingRSVP