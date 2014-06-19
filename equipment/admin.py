from django.contrib import admin
from django import forms

import base.admin
from equipment.models import *

class EquipmentInline(admin.TabularInline):
  model = Equipment

  def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    field = super(EquipmentInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

    if db_field.name == 'category':
      if request.model is not None:
        field.queryset = field.queryset.filter(model=Category.model_hash()[request.model])
      else:
        field.queryset = field.queryset.none()
    return field


class GearAdmin(base.admin.EntryAdmin):  
  list_display = ('name', 'indexes')
  fields = ['name', 'model', 'encumbrance', 'notes', 'image']
  inlines = [EquipmentInline, base.admin.IndexInline]
  
  def queryset(self, request):
    qs = super(GearAdmin, self).queryset(request)
    return qs.filter(model='Gear')
    
  def get_form(self, request, obj=None, **kwargs):
    # just save obj reference for future processing in Inline
    if not hasattr(request, 'model'):
      request.model = 'Gear'
    return super(GearAdmin, self).get_form(request, obj, **kwargs)
  
class WeaponAdmin(GearAdmin):
  fields = ['name', 'model', 'weapon_skill', 'damage', 'critical', 'weapon_range', 'encumbrance', 'hard_points', 'special', 'notes', 'image']

  def formfield_for_choice_field(self, db_field, request, **kwargs):
    if db_field.name == "weapon_skill":
      kwargs['choices'] = (
        (1, 'Brawl'),
        (2, 'Melee'),
        (3, 'Ranged [Light]'),
        (4, 'Ranged [Heavy]'),
        (5, 'Gunnery'),
        (6, 'Lightsaber'),
        (7, 'Brawl - Non Brawn'), # These are for items that do not add
        (8, 'Melee - Non Brawn'), # To the Brawn Characteristic
      )
    return super(WeaponAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)
      
  def formfield_for_dbfield(self, db_field, **kwargs):
    formfield = super(WeaponAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    if db_field.name == 'special':
      formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
    return formfield
          
  def queryset(self, request):
    qs = super(GearAdmin, self).queryset(request)
    return qs.filter(model='Weapon')
    
  def get_form(self, request, obj=None, **kwargs):
    # just save obj reference for future processing in Inline
    if not hasattr(request, 'model'):
      request.model = 'Weapon'
    return super(GearAdmin, self).get_form(request, obj, **kwargs)

class ArmorAdmin(GearAdmin):
  fields = ['name', 'defense', 'soak', 'encumbrance', 'hard_points', 'notes', 'image']

  def queryset(self, request):
    qs = super(GearAdmin, self).queryset(request)
    return qs.filter(model='Armor')
  
  def get_form(self, request, obj=None, **kwargs):
    # just save obj reference for future processing in Inline
    if not hasattr(request, 'model'):
      request.model = 'Armor'
    return super(ArmorAdmin, self).get_form(request, obj, **kwargs)

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('model', 'name')
  
  def queryset(self, request):
    qs = super(CategoryAdmin, self).queryset(request)
    return qs.filter(model__in=[x[0] for x in Category.MODEL_CHOICES])
  
class AttachmentAdmin(GearAdmin):
  fields = ['name', 'encumbrance', 'hard_points', 'notes', 'image']

  def queryset(self, request):
    qs = super(GearAdmin, self).queryset(request)
    return qs.filter(model='Attachment')

  def get_form(self, request, obj=None, **kwargs):
    # just save obj reference for future processing in Inline
    if not hasattr(request, 'model'):
      request.model = 'Attachment'
    return super(AttachmentAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Gear, GearAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Armor, ArmorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Attachment, AttachmentAdmin)
