from django.contrib import admin
from django import forms

# Register your models here.
from base.models import *

class SystemAdmin(admin.ModelAdmin):
  list_display = ('name', 'initials')

class BookAdmin(admin.ModelAdmin):
  def system_initials(self, obj):
    return obj.system.initials
  
  list_display = ('name', 'initials', 'num_pages', 'product_key', 'system_initials' )
  
class EntryAdmin(admin.ModelAdmin):
  search_fields = ['name']
  def formfield_for_dbfield(self, db_field, **kwargs):
    formfield = super(EntryAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    if db_field.name == 'notes':
      formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
    return formfield

class IndexInline(admin.TabularInline):
  model = Index
  extra = 1

admin.site.register(Entry, EntryAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Book, BookAdmin)

