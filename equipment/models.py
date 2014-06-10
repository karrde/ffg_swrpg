from django.db import models
import base.models

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

class Skill(models.Model):
  SKILL_CHOICES = (
    (1, 'Weapon'),
  )
  skill = models.IntegerField(choices=SKILL_CHOICES)
  name = models.CharField(max_length=50)

  def __unicode__(self):
    return self.name

class RangeBand(models.Model):
  RANGE_BAND_CHOICES = (
    (1, 'Weapon'),
    (2, 'Sensor'),
  )
  range_band = models.IntegerField(choices=RANGE_BAND_CHOICES)
  name = models.CharField(max_length=50)

  def __unicode__(self):
    return self.name

class EquipmentManager(models.Manager):
  def get_queryset(self):
    return super(EquipmentManager, self).get_queryset()

class Gear(base.models.Entry):
  objects = base.models.EntryManager()
  equipment = EquipmentManager()
  price = models.IntegerField()
  restricted = models.BooleanField()
  encumbrance = models.IntegerField()
  rarity = models.IntegerField()
  category = models.ForeignKey(Category)
  
  def __unicode__(self):
    return self.name
    
  def _display_price(self):
    if self.restricted:
      res = "(R) "
    else:
      res = ""
    if self.price:
      rprice = "{0:,d}".format(self.price)
    else:
      rprice = "-"
    return '{0}{1}'.format(res, rprice)

  def _display_encum(self):
    if self.price or self.encumbrance:
      return str(self.encumbrance)
    else:
      return "-"

  def _display_rarity(self):
    if self.price or self.rarity:
      return str(self.rarity)
    else:
      return "-"
      
  def _aka(self):
    akas = []
    for x in self.index_set.all():
      if x.aka:
        akas.append("{0} ({1})".format(x.aka, x.book.display_initials))
    return ", ".join(akas)
    
  display_price = property(_display_price)
  display_encum = property(_display_encum)
  display_rarity = property(_display_rarity)
  aka = property(_aka)
  
  class Meta:
    ordering = ['name']

class Weapon(Gear):
  objects = base.models.EntryManager()
  skill = models.ForeignKey(Skill)
  damage = models.IntegerField()
  critical = models.IntegerField()
  range_band = models.ForeignKey(RangeBand)
  hard_points = models.IntegerField()
  special = models.CharField(max_length=200)
  
  def _display_damage(self):
    if (self.skill.name in ['Melee', 'Brawl']):
      return "{0:+d}".format(self.damage)
    else:
      return self.damage
  
  def _display_crit(self):
    if self.critical:
      return str(self.critical)
    else:
      return "-"

  def _display_hp(self):
    if self.price or self.hard_points:
      return str(self.hard_points)
    else:
      return "-"
      
  display_crit = property(_display_crit)
  display_hp = property(_display_hp)
  display_damage = property(_display_damage)
  
    
class Armor(Gear):
  objects = base.models.EntryManager()
  defense = models.IntegerField()
  soak = models.IntegerField()
  hard_points = models.IntegerField()

  def _display_hp(self):
    if self.price or self.hard_points:
      return str(self.hard_points)
    else:
      return "-"
      
  display_hp = property(_display_hp)
    
class Attachment(Gear):
  objects = base.models.EntryManager()
  hard_points = models.IntegerField()
  
  def _display_encum(self):
    if self.price and self.encumbrance:
      return "{0:+d}".format(self.encumbrance)
    else:
      return "-"

  display_encum = property(_display_encum)

  
