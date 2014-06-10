from django.contrib import admin
from django import forms

import base.admin, equipment.models
from adversaries.models import *

class TalentEntryInline(admin.TabularInline):
  model = TalentEntry
  extra = 1

class SkillEntryInline(admin.TabularInline):
  model = SkillEntry
  extra = 1
  
class AdversaryAdmin(admin.ModelAdmin):
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
      kwargs["queryset"] = equipment.models.Gear.equipment.all()
    return super(AdversaryAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
  
  
admin.site.register(Adversary, AdversaryAdmin)
