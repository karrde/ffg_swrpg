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
    return Item.objects.filter(pk__in=[x.item.id for x in self.index_set.filter(item__category__model=1)])
  def _weapon_set(self):
    return Weapon.objects.filter(pk__in=[x.item.id for x in self.index_set.filter(item__category__model=2)])
  def _armor_set(self):
    return Armor.objects.filter(pk__in=[x.item.id for x in self.index_set.filter(item__category__model=3)])
  def _attachment_set(self):
    return Attachment.objects.filter(pk__in=[x.item.id for x in self.index_set.filter(item__category__model=4)])
  def _vehicle_set(self):
    return Vehicle.objects.filter(pk__in=[x.item.id for x in self.index_set.filter(item__category__model=5)])
  def _starship_set(self):
    return Starship.objects.filter(pk__in=[x.item.id for x in self.index_set.filter(item__category__model=6)])
    
  item_set = property(_item_set)
  weapon_set = property(_weapon_set)
  armor_set = property(_armor_set)
  attachment_set = property(_attachment_set)
  vehicle_set = property(_vehicle_set)
  starship_set = property(_starship_set)
  
class Category(models.Model):
  MODEL_CHOICES = (
    (1, 'Item'),
    (2, 'Weapon'),
    (3, 'Armor'),
    (4, 'Attachment'),
    (5, 'Vehicle'),
    (6, 'Starship'),
  )
  model = models.IntegerField(choices=MODEL_CHOICES)
  name = models.CharField(max_length=50)

  def _weapon_set(self):
    if self.model == 2:
      return Weapon.objects.filter(item_ptr_id__in=[x.id for x in self.item_set.all()])
  weapon_set = property(_weapon_set)

  def _attachment_set(self):
    if self.model == 4:
      return Attachment.objects.filter(item_ptr_id__in=[x.id for x in self.item_set.all()])
  attachment_set = property(_attachment_set)

  def _vehicle_set(self):
    if self.model == 5:
      return Vehicle.objects.filter(item_ptr_id__in=[x.id for x in self.item_set.all()])
  vehicle_set = property(_vehicle_set)

  def _starship_set(self):
    if self.model == 6:
      return Starship.objects.filter(item_ptr_id__in=[x.id for x in self.item_set.all()])
  starship_set = property(_starship_set)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ['name']

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

def get_item_image_path(instance, filename):
  if hasattr(instance, 'weapon'):
    path_start = 'weapon'
  else:
    path_start = 'item'
  return os.path.join(path_start, str(instance.id), filename)

class Item(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  restricted = models.BooleanField()
  encumbrance = models.IntegerField()
  rarity = models.IntegerField()
  category = models.ForeignKey(Category)
  image = models.ImageField(upload_to=get_item_image_path, null=True, blank=True)
  notes = models.CharField(max_length=500, blank=True)
  
  def __unicode__(self):
    return self.name
    
  def _indexes(self):
    return ", ".join([idx.str() for idx in self.index_set.all()])
    
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
  indexes = property(_indexes)
  aka = property(_aka)
  
  class Meta:
    ordering = ['name']

class Index(models.Model):
  book = models.ForeignKey(Book)
  page = models.IntegerField()
  item = models.ForeignKey(Item)
  aka = models.CharField(max_length=100, blank=True)
  
  def __unicode__(self):
    ret_str = "{0}:{1}".format(self.book.display_initials, self.page)
    if self.aka:
      ret_str += "*"
    return ret_str
    
  def str(self):
    return self.__unicode__()
  
class Weapon(Item):
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
  
  class Meta:
    ordering = ['name']
    
class Armor(Item):
  defense = models.IntegerField()
  soak = models.IntegerField()
  hard_points = models.IntegerField()

  def _display_hp(self):
    if self.price or self.hard_points:
      return str(self.hard_points)
    else:
      return "-"
      
  display_hp = property(_display_hp)

  class Meta:
    ordering = ['name']
    
class Attachment(Item):
  by_silhoutte = models.BooleanField()
  hard_points = models.IntegerField()
  
  def _display_price(self):
    item_price = super(Attachment, self)._display_price()
    if self.by_silhoutte:
      return "{0} x silhoutte".format(item_price)
    else:
      return item_price
      
  def _display_encum(self):
    if self.price and self.encumbrance:
      return "{0:+d}".format(self.encumbrance)
    else:
      return "-"

  display_price = property(_display_price)
  display_encum = property(_display_encum)

  
class Vehicle(Item):
  silhoutte = models.IntegerField()
  speed = models.IntegerField()
  handling = models.IntegerField()
  def_fore = models.IntegerField()
  def_port = models.IntegerField()
  def_starboard = models.IntegerField()
  def_aft = models.IntegerField()
  armor_value = models.IntegerField()
  hull_trauma = models.IntegerField()
  system_strain = models.IntegerField()
  model = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=100)
  max_altitude = models.IntegerField(null=True,blank=True)
  sensor_range = models.ForeignKey(RangeBand)
  passenger = models.IntegerField()
  hard_points = models.IntegerField()
  weapon_count = models.IntegerField()

  def _display_def(self):
    if self.silhoutte < 5:
      defps = "/-/-/"
    else:
      defps = "/{0}/{1}/".format(self.def_port, self.def_starboard)
    return "{0}{1}{2}".format(self.def_fore, defps, self.def_aft)
  defense = property(_display_def)
  
  def _total_defense(self):
    return self.def_fore + self.def_port + self.def_starboard + self.def_aft
  total_defense = property(_total_defense)
  
  def _display_handling(self):
    return "{0:{1}}".format(self.handling, "+" if self.handling else "")
  display_handling = property(_display_handling)

  def _crew(self):
    crew_total = 0
    for ce in self.crewentry_set.all():
      crew_total += ce.quantity
    return crew_total
  crew = property(_crew)
  
  def _crew_detail(self):
    return ", ".join([x.__unicode__() for x in self.crewentry_set.all()]).capitalize()
  crew_detail = property(_crew_detail)

  def _display_altitude(self):
    if self.max_altitude:
      suffix = 'meters'
      alt = self.max_altitude
      if alt > 1000:
        suffix = 'km'
        alt = alt // 1000
      elif alt == 1:
        suffix = 'meter'
      return "{0} {1}".format(alt, suffix)
  display_altitude = property(_display_altitude)

class CrewDescriptor(models.Model):
  description = models.CharField(max_length=100)
  def __unicode__(self):
    return self.description
  class Meta:
    ordering = ['description']

class CrewEntry(models.Model):
  quantity = models.IntegerField()
  description = models.ForeignKey(CrewDescriptor)
  vehicle = models.ForeignKey(Vehicle)
  
  def __unicode__(self):
    if self.quantity < 10:
      q = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][self.quantity]
    else:
      q = self.quantity
    plz = 0
    d = str(self.description)
    if self.quantity > 1:
      plz = 1
    if " and " in d:
      plz = 0
    if "/" in d:
      plz = 0
    if plz:
       d += "s"
    return "{0} {1}".format(q, d)
    
class Starship(Vehicle):
  NAVCOMP_CHOICES = (
    (1, 'Yes'),
    (2, 'None'),
    (3, 'Astromech Droid Socket'),
  )
  navicomputer = models.IntegerField(choices=NAVCOMP_CHOICES)
  
  def _hyperdrive(self):
    return ", ".join([str(x) for x in self.hyperdrive_set.order_by('rank')]) or 'None'
  hyperdrive = property(_hyperdrive)
  
  def _consumables(self):
    return str(self.consumable).capitalize()
  consumables  = property(_consumables)
  
  def _display_navicomputer(self):
    return dict(Starship.NAVCOMP_CHOICES)[self.navicomputer]
  display_navicomputer = property(_display_navicomputer)
  
class Hyperdrive(models.Model):
  RANK_CHOICES = (
    (1, 'Primary'),
    (2, 'Backup'),
    (3, 'Tertiary backup'),
  )
  rank = models.IntegerField(choices=RANK_CHOICES)
  class_value = models.IntegerField()
  starship = models.ForeignKey(Starship)
  
  def __unicode__(self):
    return "{0}: Class {1}".format(dict(Hyperdrive.RANK_CHOICES)[self.rank], self.class_value)
  
  
class Consumable(models.Model):
  PERIOD_CHOICES = (
    (1, 'hour'),
    (2, 'day'),
    (3, 'week'),
    (4, 'month'),
    (5, 'year'),
  )
  value = models.IntegerField()
  period = models.IntegerField(choices=PERIOD_CHOICES)
  starship = models.OneToOneField(Starship)
  
  def _sort_value(self):
    if self.period is 1:
      return value
    elif self.period is 2:
      return value * 24
    elif self.period is 3:
      return value * 24 * 7
    elif self.period is 4:
      return value * 24 * 30
    elif self.period is 5:
      return value * 24 * 365
      
  sort_value = property(_sort_value)
  
  def __unicode__(self):
    if self.value < 10:
      q = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][self.value]
    else:
      q = self.value
    return "{0} {1}".format(q, dict(Consumable.PERIOD_CHOICES)[self.period])
    
  
