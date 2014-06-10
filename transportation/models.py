from django.db import models

import base.models, equipment.models

class Category(equipment.models.Category):
  class Meta:
    proxy = True

  MODEL_CHOICES = (
    (5, 'Vehicle'),
    (6, 'Starship'),
    (7, 'VehicleAttachment'),
  )

  def _vehicle_set(self):
    if self.model == 5:
      return Vehicle.objects.filter(gear_ptr_id__in=[x.id for x in self.gear_set.all()])
  vehicle_set = property(_vehicle_set)

  def _starship_set(self):
    if self.model == 6:
      return Starship.objects.filter(gear_ptr_id__in=[x.id for x in self.gear_set.all()])
  starship_set = property(_starship_set)

class RangeBand(equipment.models.RangeBand):
  class Meta:
    proxy = True

  RANGE_BAND_CHOICES = (
    (2, 'Sensor'),
  )

  def __init__(self, *args, **kwargs):
    super(RangeBand, self).__init__(*args, **kwargs)
    self._meta.get_field_by_name('range_band')[0]._choices = RangeBand.RANGE_BAND_CHOICES

class Vehicle(equipment.models.Gear):
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
  vehicle_model = models.CharField(max_length=100)
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
    if "crew" in d:
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
    
  
class VehicleAttachment(equipment.models.Attachment):
  by_silhoutte = models.BooleanField()
  
  def _display_price(self):
    gear_price = super(VehicleAttachment, self)._display_price()
    if self.by_silhoutte:
      return "{0} x silhoutte".format(gear_price)
    else:
      return gear_price
      
  display_price = property(_display_price)
  