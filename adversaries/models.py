from django.db import models

import base.models, character.models, equipment.models

class Category(base.models.Category):
  class Meta:
    proxy = True

  MODEL_CHOICES = (
    (201, 'Adversary'),
  )


class Adversary(base.models.Entry):
  LEVEL_CHOICES = (
    ('Minion', 'Minion'),
    ('Rival', 'Rival'),
    ('Nemesis', 'Nemesis'),
  )
  level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
  brawn = models.IntegerField()
  agility = models.IntegerField()
  intellect = models.IntegerField()
  cunning = models.IntegerField()
  willpower = models.IntegerField()
  presence = models.IntegerField()
  soak_value = models.IntegerField()
  wound_threshold = models.IntegerField()
  strain_threshold = models.IntegerField(null=True, blank=True)
  melee_defense = models.IntegerField()
  ranged_defense = models.IntegerField()
  abilities = models.ManyToManyField(character.models.Ability, blank=True)
  equipment = models.ManyToManyField(equipment.models.Gear, blank=True)
  
class TalentEntry(models.Model):
  adversary = models.ForeignKey(Adversary)
  talent = models.ForeignKey(character.models.Talent)
  rank = models.IntegerField(null=True, blank=True)
  
class SkillEntry(models.Model):
  adversary = models.ForeignKey(Adversary)
  skill = models.ForeignKey(character.models.Skill)
  rank = models.IntegerField(null=True, blank=True)
  
