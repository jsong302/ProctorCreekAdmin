from tastypie.resources import ModelResource
from panel.models import Story
class StoryResource(ModelResource):
    class Meta:
        queryset = Story.objects.all()
        resource_name = 'note'