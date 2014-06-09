from django.contrib import admin
from django import forms

import base.admin
from character.models import *

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('model', 'name')
  
  def queryset(self, request):
    qs = super(CategoryAdmin, self).queryset(request)
    return qs.filter(model__in=[x[0] for x in Category.MODEL_CHOICES])

class SkillAdmin(base.admin.EntryAdmin):
  fields = ['name', 'characteristic', 'skill_type', 'category', 'notes']
  inlines = [base.admin.IndexInline]
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=102)
    return super(SkillAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(SkillAdmin, self).queryset(request)
    return qs.filter(category__model=102)
  
class TalentAdmin(base.admin.EntryAdmin):
  fields = ['name', 'category', 'activation', 'ranked', 'force_sensitive', 'notes']
  inlines = [base.admin.IndexInline]
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=103)
    return super(TalentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(TalentAdmin, self).queryset(request)
    return qs.filter(category__model=103)
  
class CareerAdmin(base.admin.EntryAdmin):
  fields = ['name', 'skills', 'category', 'image', 'notes']
  inlines = [base.admin.IndexInline]
  filter_horizontal = ('skills',)
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=104)
    return super(CareerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(CareerAdmin, self).queryset(request)
    return qs.filter(category__model=104)
  
class TalentTreeEntryInline(admin.TabularInline):
  model = TalentTreeEntry
  extra = 25
  max_num = 25

class TalentTreeAdmin(base.admin.EntryAdmin):
  fields = ['name', 'skills', 'category', 'image', 'notes']
  inlines = [TalentTreeEntryInline, base.admin.IndexInline]
  filter_horizontal = ('skills',)

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=105)
    return super(TalentTreeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(TalentTreeAdmin, self).queryset(request)
    return qs.filter(category__model=105)

class SpecializationAdmin(base.admin.EntryAdmin):
  fields = ['name', 'careers', 'skills', 'category', 'image', 'notes']
  inlines = [TalentTreeEntryInline, base.admin.IndexInline]
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=106)
    return super(SpecializationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(SpecializationAdmin, self).queryset(request)
    return qs.filter(category__model=106)
  
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
      'fields': ('category', 'notes', 'image'),
    })
  )
  
  inlines = [base.admin.IndexInline]
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=107)
    return super(SpeciesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(SpeciesAdmin, self).queryset(request)
    return qs.filter(category__model=107)
  


admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(TalentTree, TalentTreeAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Species, SpeciesAdmin)
