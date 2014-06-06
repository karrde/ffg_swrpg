from django.contrib import admin

import base.admin
from equipment.models import *

class ItemAdmin(base.admin.EntryAdmin):  
  list_display = ('name', 'price', 'encumbrance', 'rarity', 'indexes')
  fields = ['name', ('price', 'restricted'), 'encumbrance', 'rarity', 'category', 'notes', 'image']
  inlines = [base.admin.IndexInline]
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=1)
    return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(ItemAdmin, self).queryset(request)
    return qs.filter(category__model=1)

  
class WeaponAdmin(ItemAdmin):
  fields = ['name', 'skill', 'damage', 'critical', 'range_band', 'encumbrance', 'hard_points', ('price', 'restricted'), 'rarity', 'special', 'category', 'notes', 'image']

  def formfield_for_dbfield(self, db_field, **kwargs):
    formfield = super(WeaponAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    if db_field.name == 'special':
      formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
    return formfield
          
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=2)
    elif db_field.name == 'skill':
      kwargs['queryset'] = Skill.objects.filter(skill=1)
    elif db_field.name == 'range_band':
      kwargs['queryset'] = RangeBand.objects.filter(range_band=1)
    return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
  def queryset(self, request):
    qs = super(ItemAdmin, self).queryset(request)
    return qs.filter(category__model=2)
    
class ArmorAdmin(ItemAdmin):
  fields = ['name', 'defense', 'soak', ('price', 'restricted'), 'encumbrance', 'hard_points', 'rarity', 'category', 'notes', 'image']

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=3)
    return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(ItemAdmin, self).queryset(request)
    return qs.filter(category__model=3)
  
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('model', 'name')
  
class AttachmentAdmin(ItemAdmin):
  fields = ['name', ('price', 'restricted', 'by_silhoutte'), 'encumbrance', 'hard_points', 'rarity', 'category', 'notes', 'image']

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=4)
    return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(ItemAdmin, self).queryset(request)
    return qs.filter(category__model=4)

class CrewEntryInline(admin.TabularInline):
  model = CrewEntry
  extra = 1
  
class VehicleAdmin(ItemAdmin):
  fields = ['name', 'silhoutte', 'speed', 'handling', ('def_fore', 'def_port', 'def_starboard', 'def_aft'), 'armor_value', 'hull_trauma', 'system_strain', 'category', 'model',  'manufacturer', 'max_altitude', 'sensor_range', 'encumbrance', 'passenger', ('price', 'restricted'), 'rarity', 'hard_points', 'weapon_count', 'notes', 'image']
  inlines = [CrewEntryInline, base.admin.IndexInline]

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=5)
    elif db_field.name == 'sensor_range':
      kwargs['queryset'] = RangeBand.objects.filter(range_band=2)    
    return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(ItemAdmin, self).queryset(request)
    return qs.filter(category__model=5)
    
class HyperdriveInline(admin.TabularInline):
  model = Hyperdrive
  extra = 2
  max_num = 3
  
class ConsumableInline(admin.TabularInline):
  model = Consumable

class StarshipAdmin(ItemAdmin):
  fields = ['name', 'silhoutte', 'speed', 'handling', ('def_fore', 'def_port', 'def_starboard', 'def_aft'), 'armor_value', 'hull_trauma', 'system_strain', 'category', 'model',  'manufacturer', 'navicomputer', 'sensor_range', 'encumbrance', 'passenger', ('price', 'restricted'), 'rarity', 'hard_points', 'weapon_count', 'notes', 'image']
  inlines = [CrewEntryInline, HyperdriveInline, ConsumableInline, base.admin.IndexInline]

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=6)
    elif db_field.name == 'sensor_range':
      kwargs['queryset'] = RangeBand.objects.filter(range_band=2)    
    return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(ItemAdmin, self).queryset(request)
    return qs.filter(category__model=6)



admin.site.register(Item, ItemAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Armor, ArmorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Skill)
admin.site.register(RangeBand)
admin.site.register(CrewDescriptor)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Starship, StarshipAdmin)