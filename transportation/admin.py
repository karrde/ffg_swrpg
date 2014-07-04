from django.contrib import admin

import base.admin
import equipment.admin
import equipment.models
from transportation.models import *

class EquipmentInline(admin.TabularInline):
  model = equipment.models.Equipment
  extra = 1

  def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    field = super(EquipmentInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

    if db_field.name == 'category':
      if request.model is not None:
        field.queryset = field.queryset.filter(model=Category.model_hash()[request.model])
      else:
        field.queryset = field.queryset.none()
    return field

class CrewEntryInline(admin.TabularInline):
  model = CrewEntry
  extra = 1
  
class VehicleAdmin(equipment.admin.GearAdmin):
  fields = ['name', 'silhoutte', 'speed', 'handling', ('def_fore', 'def_port', 'def_starboard', 'def_aft'), 'armor_value', 'hull_trauma', 'system_strain', 'vehicle_model', 'manufacturer', 'max_altitude', 'sensor_range', 'encumbrance', 'passenger', 'hard_points', 'weapon_count', 'notes', 'image']
  inlines = [CrewEntryInline, EquipmentInline, base.admin.IndexInline]

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'sensor_range':
      kwargs['queryset'] = RangeBand.objects.filter(range_band=2)    
    return super(equipment.admin.GearAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(equipment.admin.GearAdmin, self).queryset(request)
    return qs.filter(model='Vehicle')
    
  def get_form(self, request, obj=None, **kwargs):
    # just save obj reference for future processing in Inline
    if not hasattr(request, 'model'):
      request.model = 'Vehicle'
    return super(VehicleAdmin, self).get_form(request, obj, **kwargs)

class HyperdriveInline(admin.TabularInline):
  model = Hyperdrive
  extra = 2
  max_num = 3
  
class ConsumableInline(admin.TabularInline):
  model = Consumable

class StarshipAdmin(equipment.admin.GearAdmin):
  fields = ['name', 'silhoutte', 'speed', 'handling', ('def_fore', 'def_port', 'def_starboard', 'def_aft'), 'armor_value', 'hull_trauma', 'system_strain', 'vehicle_model', 'manufacturer', 'navicomputer', 'sensor_range', 'encumbrance', 'passenger', 'hard_points', 'weapon_count', 'notes', 'image']
  inlines = [CrewEntryInline, HyperdriveInline, ConsumableInline, EquipmentInline, base.admin.IndexInline]

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=6)
    elif db_field.name == 'sensor_range':
      kwargs['queryset'] = RangeBand.objects.filter(range_band=2)    
    return super(equipment.admin.GearAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(equipment.admin.GearAdmin, self).queryset(request)
    return qs.filter(model='Starship')

  def get_form(self, request, obj=None, **kwargs):
    # just save obj reference for future processing in Inline
    if not hasattr(request, 'model'):
      request.model = 'Starship'
    return super(StarshipAdmin, self).get_form(request, obj, **kwargs)

class VehicleAttachmentAdmin(equipment.admin.GearAdmin):
  fields = ['name', 'by_silhoutte', 'encumbrance', 'hard_points', 'notes', 'image']
  inlines = [EquipmentInline, base.admin.IndexInline]
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=7)
    return super(equipment.admin.GearAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(equipment.admin.GearAdmin, self).queryset(request)
    return qs.filter(model='VehicleAttachment')

  def get_form(self, request, obj=None, **kwargs):
    # just save obj reference for future processing in Inline
    if not hasattr(request, 'model'):
      request.model = 'VehicleAttachment'
    return super(VehicleAttachmentAdmin, self).get_form(request, obj, **kwargs)

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

