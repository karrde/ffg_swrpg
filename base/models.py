from django.db import models
import os
from django.db.models.signals import pre_save
from django.dispatch import receiver

class System(models.Model):
  name = models.CharField(max_length=100)
  initials = models.CharField(max_length=10)
  def __unicode__(self):
    return self.name
  
class Book(models.Model):
  name = models.CharField(max_length=100)
  initials = models.CharField(max_length=10)
  num_pages = models.IntegerField()
  system = models.ForeignKey(System)
  product_key = models.CharField(max_length=10)
  def __unicode__(self):
    return "{0} ({1})".format(self.name, self.system.initials)
    
  def is_unique(self):
    if Book.objects.filter(initials=self.initials).count() > 1:
      return False
    else:
      return True
  
  def _display_initials(self):
    if self.is_unique():
      return self.initials
    else:
      return "{0}-{1}".format(self.system.initials[0], self.initials)
  display_initials = property(_display_initials)
  
  def _entry_set(self):
    return [Entry.objects.get(pk=x.entry.id) for x in self.index_set.order_by('page', 'entry__name')]
  entry_set = property(_entry_set)
  
def get_item_image_path(instance, filename):
  if hasattr(instance, 'weapon'):
    path_start = 'weapon'
  else:
    path_start = 'item'
  return os.path.join(path_start, str(instance.id), filename)

class EntryManager(models.Manager):
  def get_queryset(self):
    return super(EntryManager, self).get_queryset().filter(model=self.model.__name__)

class Entry(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to=get_item_image_path, null=True, blank=True)
  notes = models.CharField(max_length=500, blank=True)
  model = models.CharField(max_length=100)

  def __unicode__(self):
    return self.name

  def _indexes(self):
    return ", ".join([idx.str() for idx in self.index_set.all()])
  indexes = property(_indexes)

  def _aka(self):
    akas = []
    for x in self.index_set.all():
      if x.aka:
        akas.append("{0} ({1})".format(x.aka, x.book.display_initials))
    return ", ".join(akas)
  aka = property(_aka)
  
  def name_link(self):
    return '<a href="{link}" class="{model}_name">{name}</a>'.format(link=self.get_absolute_url(), name=self.name, model=self.model.lower())
    
  @receiver(pre_save)
  def my_callback(sender, instance, *args, **kwargs):
    if Entry in instance._meta.get_parent_list():
      if not instance.model:
        instance.model = instance.__class__.__name__

  def clean(self, *args, **kwargs):
    super(Entry, self).clean(*args, **kwargs)
    if not self.model:
      self.model = self.__class__.__name__

  @models.permalink
  def get_absolute_url(self):
      return ('{0}:{1}'.format(self.__class__._meta.app_label, self.model.lower()), [str(self.id)])

  class Meta:
    ordering = ['name']

class Index(models.Model):
  book = models.ForeignKey(Book)
  page = models.IntegerField()
  entry = models.ForeignKey(Entry)
  aka = models.CharField(max_length=100, blank=True)

  def __unicode__(self):
    ret_str = "{0}:{1}".format(self.book.display_initials, self.page)
    if self.aka:
      ret_str += "*"
    return ret_str

  def str(self):
    return self.__unicode__()

  class Meta:
    ordering = ['book__product_key', 'page', 'entry__name']

