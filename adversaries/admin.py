from django.contrib import admin
from django import forms

import base.admin, equipment.admin, equipment.models
from adversaries.models import *

class TalentEntryInline(admin.TabularInline):
  model = TalentEntry
  extra = 1

class SkillEntryInline(admin.TabularInline):
  model = SkillEntry
  extra = 1
  
class AdversaryAdmin(base.admin.EntryAdmin):
  fieldsets = (
    (None, {
      'fields': ('name', 'level'),
    }),
    ('Stat Fields', {
      'fields': (('brawn', 'agility', 'intellect', 'cunning', 'willpower', 'presence'), 'soak_value', 'wound_threshold', 'strain_threshold', 'melee_defense', 'ranged_defense'),
    }),
    ('Other', {
      'fields': ('abilities','equipment',),
    }),
    ('Base Fields', {
      'fields': ('notes', 'image'),
    })
  )
  
  inlines = [TalentEntryInline, SkillEntryInline, base.admin.IndexInline]
  filter_horizontal = ('abilities', 'equipment',)
  
  def formfield_for_manytomany(self, db_field, request, **kwargs):
    if db_field.name == "equipment":
      kwargs["queryset"] = equipment.models.Gear.objects.filter(model__in=['Gear', 'Weapon', 'Armor'])
    return super(AdversaryAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
admin.site.register(Adversary, AdversaryAdmin)


class CreatureWeaponAdmin(equipment.admin.WeaponAdmin):
  list_display = ('__unicode__',)
  fields = ['species', 'name', 'weapon_skill', 'damage', 'critical', 'weapon_range', 'special', 'notes', 'image']
  inlines = [base.admin.IndexInline]

  def queryset(self, request):
    qs = super(equipment.admin.GearAdmin, self).queryset(request)
    return qs.filter(model='CreatureWeapon')

  def get_form(self, request, obj=None, **kwargs):
    # just save obj reference for future processing in Inline
    if not hasattr(request, 'model'):
      request.model = 'CreatureWeapon'
    return super(equipment.admin.GearAdmin, self).get_form(request, obj, **kwargs)
admin.site.register(CreatureWeapon, CreatureWeaponAdmin)

class CreatureAdmin(AdversaryAdmin):
  fieldsets = (
    (None, {
      'fields': ('name', 'species', 'level'),
    }),
    ('Stat Fields', {
      'fields': (('brawn', 'agility', 'intellect', 'cunning', 'willpower', 'presence'), 'soak_value', 'wound_threshold', 'strain_threshold', 'melee_defense', 'ranged_defense'),
    }),
    ('Base Fields', {
      'fields': ('notes', 'image'),
    })
  )
  
  inlines = [TalentEntryInline, SkillEntryInline, base.admin.IndexInline]
admin.site.register(Creature, CreatureAdmin)
  

