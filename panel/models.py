from django.db import models

# Create your models here.

from django.utils import timezone
import os



class Story(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    abstract = models.TextField(null=True, blank=True)
    details = models.TextField()
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
        return self.name

class StoryImage(models.Model):

    def get_story_image_path(instance, filename):
        return os.path.join(
            "stories/%d/images" % instance.story.id)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_story_image_path)
    caption = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.story.name


