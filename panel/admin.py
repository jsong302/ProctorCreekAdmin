from django.contrib import admin
from .models import Story, StoryImage

admin.site.register(Story)
# Register your models here.
admin.site.register(StoryImage)