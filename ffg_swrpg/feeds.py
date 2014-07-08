from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from base.models import Entry
from equipment.models import Gear
from blog.models import Blog

class BlogFeed(Feed):
  title = "FFG Star Wars RPG Index Blog Feed"
  link = '/blog'
  description = 'Latest blog entries for the RPG Index'
  
  def items(self):
    return Blog.objects.order_by('-posting_date')[:10]
    
  def item_title(self, item):
    return item.title
    
  def item_description(self, item):
    return item.blog_entry
    
  def item_link(self, item):
    return reverse('blog', args=[item.id])

class EntryFeed(Feed):
    title = "FFG Star Wars RPG Index Feed"
    link = "/entries/"
    description = "Latest added entries for the RPG Index"

    def items(self):
        return Entry.objects.order_by('-id')[:100]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.model

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
      try:
        subitem = getattr(item, 'gear')
      except Entry.DoesNotExist:
        subitem = item
        try:
          subitem = getattr(item, 'adversary')
        except Entry.DoesNotExist:
          pass
        subitem = getattr(subitem, item.model.lower())
      else:
        try:
          subitem = getattr(subitem, 'vehicle')
        except Gear.DoesNotExist:
          pass 
        try:
          subitem = getattr(subitem, 'weapon')
        except Gear.DoesNotExist: 
          pass
        try:
          subitem = getattr(subitem, 'attachment')
        except Gear.DoesNotExist:
          pass
        subitem = getattr(subitem, subitem.model.lower())
      
      return reverse('{0}:{1}'.format(subitem.__class__._meta.app_label, subitem.model.lower()), args=[subitem.pk])
