from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import base.models, character.models, equipment.models

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
  skills = models.ManyToManyField(character.models.Skill, through='SkillEntry')
  talents = models.ManyToManyField(character.models.Talent, through='TalentEntry')
  abilities = models.ManyToManyField(character.models.Ability, blank=True)
  equipment = models.ManyToManyField(equipment.models.Gear)
  
  def _display_skills(self):
    if self.level == 'Minion':
      return ", ".join([str(x) for x in self.skills.all()]) or 'None'
  display_skills = property(_display_skills)
  
  def _display_talents(self):
    return ", ".join([str(x) for x in self.talententry_set.all()]) or 'None'
  display_talents = property(_display_talents)
  
  def _display_abilities(self):
    return ", ".join([str(x) for x in self.abilities.all()]) or 'None'
  display_abilities = property(_display_abilities)
  
  def _display_equipment(self):
    return ", ".join([str(x) for x in self.equipment.all()]) or 'None'
  display_equipment = property(_display_equipment)
  
class TalentEntry(models.Model):
  adversary = models.ForeignKey(Adversary)
  talent = models.ForeignKey(character.models.Talent)
  rank = models.IntegerField(null=True, blank=True)
  
  def __unicode__(self):
    if self.talent.ranked:
      return "{0} {1}".format(self.talent.name, self.rank)
    else:
      return self.talent.name
  
class SkillEntry(models.Model):
  adversary = models.ForeignKey(Adversary)
  skill = models.ForeignKey(character.models.Skill)
  rank = models.IntegerField(null=True, blank=True)
  
