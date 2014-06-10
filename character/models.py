from django.db import models
import base.models

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
  SKILL_TYPES = (
    (1, 'General'),
    (2, 'Combat'),
    (3, 'Knowledge'),
  )
  
  characteristic = models.IntegerField(choices=Characteristic.LIST)
  skill_type = models.IntegerField(choices=SKILL_TYPES)

  def __unicode__(self):
    return self.name

class Talent(base.models.Entry):
  ACTIVATION_CHOICES = (
    (1, 'Passive'),
    (2, 'Active'),
    (3, 'Active (Action)'),
    (4, 'Active (Maneuver)'),
    (5, 'Active (Incedential)'),
    (6, 'Active (Incedential, Out of Turn)'),
  )
  ranked = models.BooleanField()
  activation = models.IntegerField(choices=ACTIVATION_CHOICES)
  force_sensitive = models.BooleanField()
  tree_text = models.CharField(max_length=200)
  
class Career(base.models.Entry):
  skills = models.ManyToManyField(Skill)
  
class TalentTree(base.models.Entry):
  skills = models.ManyToManyField(Skill)

class TalentTreeEntry(models.Model):
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
  talent_tree = models.ForeignKey(TalentTree)
  talent = models.ForeignKey(Talent)
  cost = models.IntegerField(choices=COST_CHOICES)
  tree_column = models.IntegerField(choices=COLUMN_CHOICES)
  link_north = models.BooleanField()
  link_east = models.BooleanField()
  link_south = models.BooleanField()
  link_west = models.BooleanField()
  
class Specialization(TalentTree):
  careers = models.ManyToManyField(Career)

class Ability(base.models.Entry):
  description = models.CharField(max_length=200)
  rules_effect = models.CharField(max_length=500, blank=True)

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
  abilities = models.ManyToManyField(Ability, blank=True)
  
  