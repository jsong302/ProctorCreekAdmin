from tastypie.resources import ModelResource
from panel.models import Story
from tastypie import fields, utils

class StoryResource(ModelResource):
    images = fields.ToManyField('panel.resources.StoryImageResource', 'storyimage_set', null=True)
    class Meta:
        queryset = Story.objects.all()
        resource_name = 'story'

class StoryImageResource(ModelResource):
    story = fields.ToOneField(StoryResource, 'story')
    class Meta:
        queryset = Story.objects.all()
        resource_name = 'storyimage'