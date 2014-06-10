from django.contrib import admin
from django import forms

import base.admin
from character.models import *

class SkillAdmin(base.admin.EntryAdmin):
  fields = ['name', 'characteristic', 'skill_type', 'notes']
  inlines = [base.admin.IndexInline]
    
class TalentAdmin(base.admin.EntryAdmin):
  fields = ['name', 'activation', 'ranked', 'force_sensitive', 'notes']
  inlines = [base.admin.IndexInline]
  
class AbilityAdmin(base.admin.EntryAdmin):
  fields = ['name', 'description', 'notes']
  inlines = [base.admin.IndexInline]

class CareerAdmin(base.admin.EntryAdmin):
  fields = ['name', 'skills', 'image', 'notes']
  inlines = [base.admin.IndexInline]
  filter_horizontal = ('skills',)
  
class TalentTreeEntryInline(admin.TabularInline):
  model = TalentTreeEntry
  extra = 25
  max_num = 25

class TalentTreeAdmin(base.admin.EntryAdmin):
  fields = ['name', 'skills', 'image', 'notes']
  inlines = [TalentTreeEntryInline, base.admin.IndexInline]
  filter_horizontal = ('skills',)

class SpecializationAdmin(base.admin.EntryAdmin):
  fields = ['name', 'careers', 'skills', 'image', 'notes']
  inlines = [TalentTreeEntryInline, base.admin.IndexInline]
  
class SpeciesAdmin(base.admin.EntryAdmin):
  fieldsets = (
    (None, {
      'fields': ('name', 'player_race'),
    }),
    ('Player Race Fields', {
      'classes': ('collapse',),
      'fields': (('base_brawn', 'base_agility', 'base_intellect', 'base_cunning', 'base_willpower', 'base_presence'), 'wound_threshold_modifier', 'strain_threshold_modifier', 'starting_experience', 'special_abilities'),
    }),
    ('Bese Fields', {
      'fields': ('notes', 'image'),
    })
  )
  
  inlines = [base.admin.IndexInline]
  


admin.site.register(Skill, SkillAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(TalentTree, TalentTreeAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Species, SpeciesAdmin)
