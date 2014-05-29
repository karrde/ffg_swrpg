from django.contrib import admin
from django import forms

# Register your models here.
from books.models import System, Book, Index, Item, Weapon, Category, Skill, RangeBand, Armor

class SystemAdmin(admin.ModelAdmin):
  list_display = ('name', 'initials')

class BookAdmin(admin.ModelAdmin):
  def system_initials(self, obj):
    return obj.system.initials
  
  list_display = ('name', 'initials', 'num_pages', 'product_key', 'system_initials' )

class IndexInline(admin.TabularInline):
  model = Index
  extra = 1

class ItemAdmin(admin.ModelAdmin):  
  list_display = ('name', 'price', 'encumbrance', 'rarity', 'indexes')
  fields = ['name', ('price', 'restricted'), 'encumbrance', 'rarity', 'category', 'image']
  inlines = [IndexInline]
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=1)
    return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(ItemAdmin, self).queryset(request)
    return qs.filter(category__model=1)

  
class WeaponAdmin(ItemAdmin):
  fields = ['name', 'skill', 'damage', 'critical', 'range_band', 'encumbrance', 'hard_points', ('price', 'restricted'), 'rarity', 'special', 'category', 'image']

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
  fields = ['name', 'defense', 'soak', ('price', 'restricted'), 'encumbrance', 'hard_points', 'rarity', 'category']

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'category':
      kwargs['queryset'] = Category.objects.filter(model=3)
    return super(ItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def queryset(self, request):
    qs = super(ItemAdmin, self).queryset(request)
    return qs.filter(category__model=3)
  
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('model', 'name')

admin.site.register(System, SystemAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Armor, ArmorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill)
admin.site.register(RangeBand)