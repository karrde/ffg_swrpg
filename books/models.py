from django.db import models
import os

import base.models

class Book(base.models.Book):
  class Meta:
    proxy = True
    
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
  
