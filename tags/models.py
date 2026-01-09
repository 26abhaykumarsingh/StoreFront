from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Tag(models.Model):
  label = models.CharField(max_length=255)



class TaggedItem(models.Model):
  # What tag applied to what object
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  # To define a generic relationship we need three things
  # Type (product, video, article)      # we can get table using this
  # ID       # we can get record using this
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # contenttype is pre installed app by django, using this we can create generic relationships between our models
  object_id = models.PositiveIntegerField() # we can get the id of the object using this
  content_object = GenericForeignKey() # use this to get the actual object