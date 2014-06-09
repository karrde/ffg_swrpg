from django.db import models
import base.models

class Category(base.models.Category):
  class Meta:
    proxy = True

  MODEL_CHOICES = (
    (101, 'Characteristic'),
    (102, 'Skill'),
    (103, 'Talent'),
    (104, 'Career'),
    (105, 'Specialization'),
    (106, 'Species'),
  )
  
class Characteristic(base.models.Entry):
  class Meta:
    proxy = True
    
  LIST = (
    (1, 'Brawn'),
    (2, 'Agility'),
    (3, 'Intellect'),
    (4, 'Cunning'),
    (5, 'Willpower'),
    (6, 'Presence'),
  )

class Skill(base.models.Entry):
  characteristic = models.IntegerField(choices=Characteristic.LIST)

class Talent(base.models.Entry):
  ranked = models.BooleanField()
  
class Career(base.models.Entry):
  skills = models.ManyToManyField(Skill)
  
class Specialization(base.models.Entry):
  skills = models.ManyToManyField(Skill)
  careers = models.ManyToManyField(Career)
  
class SpecTalentEntry(models.Model):
  COST_CHOICES = (
    (5, '5'),
    (10, '10'),
    (15, '15'),
    (20, '20'),
    (25, '25'),
  )
  COLUMN_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),    
  )
  specialization = models.ForeignKey(Specialization)
  talent = models.ForeignKey(Talent)
  cost = models.IntegerField(choices=COST_CHOICES)
  tree_column = models.IntegerField(choices=COLUMN_CHOICES)
  link_north = models.BooleanField()
  link_east = models.BooleanField()
  link_south = models.BooleanField()
  link_west = models.BooleanField()
  
class Species(base.models.Entry):
  player_race = models.BooleanField()
  base_brawn = models.IntegerField(default=0)
  base_agility = models.IntegerField(default=0)
  base_intellect = models.IntegerField(default=0)
  base_cunning = models.IntegerField(default=0)
  base_willpower = models.IntegerField(default=0)
  base_presence = models.IntegerField(default=0)
  wound_threshold_modifier = models.IntegerField(default=0)
  strain_threshold_modifier = models.IntegerField(default=0)
  starting_experience = models.IntegerField(default=0)
  special_abilities = models.CharField(max_length=500, blank=True)
  
  