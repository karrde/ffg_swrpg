from django.db import models

# Create your models here.

class Blog(models.Model):
  title = models.CharField(max_length=100)
  blog_entry = models.TextField()
  entered_date = models.DateTimeField(auto_now_add=True)
  posting_date = models.DateTimeField()
  last_modified = models.DateTimeField(auto_now=True)
  
  def __unicode__(self):
    return self.title