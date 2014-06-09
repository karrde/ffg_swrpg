from django.contrib import admin
from django import forms

import base.admin
from adversaries.models import *

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('model', 'name')
  
  def queryset(self, request):
    qs = super(CategoryAdmin, self).queryset(request)
    return qs.filter(model__in=[x[0] for x in Category.MODEL_CHOICES])


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
      'fields': ('category', 'notes', 'image'),
    })
  )
  
  inlines = [TalentEntryInline, SkillEntryInline, base.admin.IndexInline]
  filter_horizontal = ('abilities', 'equipment')

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=201)
    return super(AdversaryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(AdversaryAdmin, self).queryset(request)
    return qs.filter(category__model=201)
  
admin.site.register(Category, CategoryAdmin)
admin.site.register(Adversary, AdversaryAdmin)
