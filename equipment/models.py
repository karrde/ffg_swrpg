from django.db import models
import base.models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.utils.html import strip_tags

class Category(models.Model):
  MODEL_CHOICES = (
    (1, 'Gear'),
    (2, 'Weapon'),
    (3, 'Armor'),
    (4, 'Attachment'),
  )

  model = models.IntegerField(choices=MODEL_CHOICES)
  name = models.CharField(max_length=50)

  @classmethod
  def model_hash(cls):
    return { v[1]:v[0] for i,v in enumerate(cls.MODEL_CHOICES) }

  @classmethod
  def model_numbers(cls):
    mhash = cls.model_hash()
    return [mhash[i] for i in mhash.keys()]

  def model_info(self):
    return {'id': int(self.model), 'name': self.get_model_display() }

  def __init__(self, *args, **kwargs):
    super(Category, self).__init__(*args, **kwargs)
    self._meta.get_field_by_name('model')[0]._choices = self.__class__.MODEL_CHOICES

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ['name']

  def _weapon_set(self):
    if self.model == 2:
      return Weapon.objects.filter(gear_ptr_id__in=[x.id for x in self.gear_set.all()])
  weapon_set = property(_weapon_set)

  def _attachment_set(self):
    if self.model == 4:
      return Attachment.objects.filter(gear_ptr_id__in=[x.id for x in self.gear_set.all()])
  attachment_set = property(_attachment_set)

class GearManager(models.Manager):
  def get_queryset(self):
    return super(GearManager, self).get_queryset()

class Gear(base.models.Entry):
  encumbrance = models.IntegerField(default=0)

  def _equipment_display(self, brawn=0):
    if 'Weapon' in self.model:
      damage = self.weapon.damage
      if self.weapon.weapon_skill in [1,2]:
        damage += brawn
      return "{name} ({attribs})".format(name=self.name_link(), attribs="; ".join(
        [
          self.weapon.get_weapon_skill_display(), 
          "Damage {damage}".format(damage=damage),
          "Critical {critical}".format(critical=self.weapon.display_crit),
          "Range ({range})".format(range=self.weapon.get_weapon_range_display()),
        ] + ([self.weapon.display_special] if self.weapon.display_special else [])
      ))
    elif 'Armor' in self.model:
      attribs = []
      if self.armor.soak: attribs.append("{soak:+d} soak".format(soak=self.armor.soak)) 
      if self.armor.defense: attribs.append("{defense:+d} defense".format(defense=self.armor.defense))
      return "{name} ({attribs})".format(name=self.name_link(), attribs="; ".join(attribs))
    else:
      return self.name_link()
  equipment_display = property(_equipment_display)
  
  def __unicode__(self):
    return strip_tags(self.equipment_display)
    
  def _equipment(self):
    return self.equipment_set.first()
  equipment = property(_equipment)
    
  class Meta:
    ordering = ['name']

class Equipment(models.Model):
  price = models.IntegerField()
  restricted = models.BooleanField()
  rarity = models.IntegerField()
  category = models.ForeignKey(Category)
  gear = models.ForeignKey(Gear)

  def _display_price(self):
    return '{restricted}{price:,d}'.format(restricted=["","(R) "][self.restricted], price=self.price)
  display_price = property(_display_price)
  

class Weapon(Gear):
  SKILL_CHOICES = (
    (1, 'Brawl'),
    (2, 'Melee'),
    (3, 'Ranged [Light]'),
    (4, 'Ranged [Heavy]'),
    (5, 'Gunnery'),
    (6, 'Lightsaber'),
    (7, 'Brawl'), # These are for items that do not add
    (8, 'Melee'), # To the Brawn Characteristic
  )
  RANGE_CHOICES = (  
    (1, 'Engaged'),
    (2, 'Short'),
    (3, 'Medium'),
    (4, 'Long'),
    (5, 'Extreme'),
  )
  weapon_skill = models.IntegerField(choices=SKILL_CHOICES)
  damage = models.IntegerField()
  critical = models.IntegerField()
  weapon_range = models.IntegerField(choices=RANGE_CHOICES)
  hard_points = models.IntegerField(default=0)
  special = models.CharField(max_length=200, null=True, blank=True)
  
  def _display_special(self):
    return ", ".join([str(x) for x in self.weaponqualityentry_set.all()]+[self.special])
  display_special = property(_display_special)
  
  def _display_damage(self):
    if (self.weapon_skill in [1, 2]):
      return "{0:+d}".format(self.damage)
    else:
      return self.damage
  display_damage = property(_display_damage)
  
  def _display_crit(self):
    if self.critical:
      return str(self.critical)
    else:
      return "-"
  display_crit = property(_display_crit)

  def _display_hp(self):
    return str(self.hard_points)
  display_hp = property(_display_hp)
    
class WeaponQuality(base.models.Entry):
  active = models.BooleanField()
  ranked = models.BooleanField()
  activation_cost = models.IntegerField(default=2)
  effect = models.TextField(max_length=500)
  activation_cost_mod = models.IntegerField(default=0)
  activation_cost_by_sil = models.IntegerField(default=0)
  weapons = models.ManyToManyField(Weapon, through='WeaponQualityEntry')

  def _display_active(self):
    return "Active" if self.active else "Passive"
  display_active = property(_display_active)

  def _display_ranked(self):
    return "Yes" if self.ranked else "No"
  display_ranked = property(_display_ranked)

class WeaponQualityEntry(models.Model):
  weapon = models.ForeignKey(Weapon)
  quality = models.ForeignKey(WeaponQuality)
  rank = models.IntegerField(null=True, blank=True)

  def clean(self, *args, **kwargs):
    super(WeaponQualityEntry, self).clean(*args, **kwargs)
    if self.quality.ranked:
      if self.rank < 1:
        raise ValidationError("{quality} is ranked, must have value".format(quality=self.quality.name))
    else:
      self.rank = None

  def __unicode__(self):
    if self.quality.ranked:
      return "{0} {1}".format(self.quality.name_link(), self.rank)
    else:
      return self.quality.name_link()

class Armor(Gear):
  defense = models.IntegerField()
  soak = models.IntegerField()
  hard_points = models.IntegerField()

  def _display_hp(self):
    return str(self.hard_points)
      
  display_hp = property(_display_hp)
    
class Attachment(Gear):
  hard_points = models.IntegerField()
  
  def _display_encum(self):
    if self.price and self.encumbrance:
      return "{0:+d}".format(self.encumbrance)
    else:
      return "-"

  display_encum = property(_display_encum)

