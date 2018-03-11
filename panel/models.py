from django.db import models

# Create your models here.

from django.utils import timezone


class Story(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    details = models.TextField()
    images = models.ImageField()
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    long = models.DecimalField(max_digits=10, decimal_places=8)
    created_date = models.DateTimeField(
            default=timezone.now)
    modified_date = models.DateTimeField(
            blank=True, null=True)

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title