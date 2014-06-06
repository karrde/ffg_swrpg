from django.db import models
import os

# Create your models here.

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
    
    
  def _item_set(self):
    return [Item.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__item__category__model=1).order_by('page', 'entry__name')]
  def _weapon_set(self):
    return [Weapon.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__item__category__model=2).order_by('page', 'entry__name')]
  def _armor_set(self):
    return [Armor.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__item__category__model=3).order_by('page', 'entry__name')]
  def _attachment_set(self):
    return [Attachment.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__item__category__model=4).order_by('page', 'entry__name')]
  def _vehicle_set(self):
    return [Vehicle.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__item__category__model=5).order_by('page', 'entry__name')]
  def _starship_set(self):
    return [Starship.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__item__category__model=6).order_by('page', 'entry__name')]
    
  item_set = property(_item_set)
  weapon_set = property(_weapon_set)
  armor_set = property(_armor_set)
  attachment_set = property(_attachment_set)
  vehicle_set = property(_vehicle_set)
  starship_set = property(_starship_set)
  
def get_item_image_path(instance, filename):
  if hasattr(instance, 'weapon'):
    path_start = 'weapon'
  else:
    path_start = 'item'
  return os.path.join(path_start, str(instance.id), filename)

class Entry(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to=get_item_image_path, null=True, blank=True)
  notes = models.CharField(max_length=500, blank=True)
  def __unicode__(self):
    return self.name

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

