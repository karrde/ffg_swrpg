from django import template
register = template.Library()

@register.simple_tag
def sort_table_by(request, value):
  dict_ = request.GET.copy()
  field = 'order_by'
  if field in dict_.keys() and dict_[field].lstrip('-') == value:
    if dict_[field].startswith('-'):
    # click twice on same column, revert ascending/descending
      dict_[field] = value
    else:
      dict_[field] = "-"+value
  else:
    dict_[field] = value
  ret = "?order_by={0}".format(dict_[field])
  if 'flatened' in dict_.keys() and dict_['flatened'] == 'true':
    ret += "&flatened=true"
  return ret