from django.db import models

# Create your models here.
class Pictures(models.Model):
    name = models.CharField(max_length=200)
    status = models.NullBooleanField(default=None, blank=True, null=True)
    likes = models.IntegerField(default=0)
    url = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ('id',)