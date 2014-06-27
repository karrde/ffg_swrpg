from django.db import models
import os

import base.models
from equipment.models import *
from transportation.models import *
from character.models import *
from adversaries.models import *

class Book(base.models.Book):
  class Meta:
    proxy = True
    
  def _gear_set(self):
    return [Gear.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Gear').order_by('page', 'entry__name')]
  def _weapon_set(self):
    return [Weapon.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Weapon').order_by('page', 'entry__name')]
  def _armor_set(self):
    return [Armor.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Armor').order_by('page', 'entry__name')]
  def _attachment_set(self):
    return [Attachment.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Attachment').order_by('page', 'entry__name')]
  def _vehicle_set(self):
    return [Vehicle.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Vehicle').order_by('page', 'entry__name')]
  def _starship_set(self):
    return [Starship.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Starship').order_by('page', 'entry__name')]
  def _skill_set(self):
    return [Skill.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Skill').order_by('page', 'entry__name')]
  def _talent_set(self):
    return [Talent.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Talent').order_by('page', 'entry__name')]
  def _ability_set(self):
    return [Ability.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Ability').order_by('page', 'entry__name')]
  def _adversary_set(self):
    return [Adversary.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Adversary').order_by('page', 'entry__name')]
  def _creature_set(self):
    return [Creature.objects.get(pk=x.entry.id) for x in self.index_set.filter(entry__model='Creature').order_by('page', 'entry__name')]
    
  gear_set = property(_gear_set)
  weapon_set = property(_weapon_set)
  armor_set = property(_armor_set)
  attachment_set = property(_attachment_set)
  vehicle_set = property(_vehicle_set)
  starship_set = property(_starship_set)
  skill_set = property(_skill_set)
  talent_set = property(_talent_set)
  ability_set = property(_ability_set)
  adversary_set = property(_adversary_set)
  creature_set = property(_creature_set)
                   
