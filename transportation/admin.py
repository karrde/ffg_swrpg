from django.contrib import admin

import base.admin
import equipment.admin
from transportation.models import *

class CrewEntryInline(admin.TabularInline):
  model = CrewEntry
  extra = 1
  
class VehicleAdmin(equipment.admin.GearAdmin):
  fields = ['name', 'silhoutte', 'speed', 'handling', ('def_fore', 'def_port', 'def_starboard', 'def_aft'), 'armor_value', 'hull_trauma', 'system_strain', 'category', 'model',  'manufacturer', 'max_altitude', 'sensor_range', 'encumbrance', 'passenger', ('price', 'restricted'), 'rarity', 'hard_points', 'weapon_count', 'notes', 'image']
  inlines = [CrewEntryInline, base.admin.IndexInline]

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=5)
    elif db_field.name == 'sensor_range':
      kwargs['queryset'] = RangeBand.objects.filter(range_band=2)    
    return super(equipment.admin.GearAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(equipment.admin.GearAdmin, self).queryset(request)
    return qs.filter(category__model=5)
    
class HyperdriveInline(admin.TabularInline):
  model = Hyperdrive
  extra = 2
  max_num = 3
  
class ConsumableInline(admin.TabularInline):
  model = Consumable

class StarshipAdmin(equipment.admin.GearAdmin):
  fields = ['name', 'silhoutte', 'speed', 'handling', ('def_fore', 'def_port', 'def_starboard', 'def_aft'), 'armor_value', 'hull_trauma', 'system_strain', 'category', 'model',  'manufacturer', 'navicomputer', 'sensor_range', 'encumbrance', 'passenger', ('price', 'restricted'), 'rarity', 'hard_points', 'weapon_count', 'notes', 'image']
  inlines = [CrewEntryInline, HyperdriveInline, ConsumableInline, base.admin.IndexInline]

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=6)
    elif db_field.name == 'sensor_range':
      kwargs['queryset'] = RangeBand.objects.filter(range_band=2)    
    return super(equipment.admin.GearAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(equipment.admin.GearAdmin, self).queryset(request)
    return qs.filter(category__model=6)

class VehicleAttachmentAdmin(equipment.admin.GearAdmin):
  fields = ['name', ('price', 'restricted', 'by_silhoutte'), 'encumbrance', 'hard_points', 'rarity', 'category', 'notes', 'image']

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=7)
    return super(equipment.admin.GearAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(equipment.admin.GearAdmin, self).queryset(request)
    return qs.filter(category__model=7)

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('model', 'name')
  
  def queryset(self, request):
    qs = super(CategoryAdmin, self).queryset(request)
    return qs.filter(model__in=[x[0] for x in Category.MODEL_CHOICES])

admin.site.register(CrewDescriptor)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Starship, StarshipAdmin)
admin.site.register(VehicleAttachment, VehicleAttachmentAdmin)

