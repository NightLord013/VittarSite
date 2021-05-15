from django.template.library import Library
from django.template.defaultfilters import stringfilter

register = Library()

@register.filter
@stringfilter
def rightzeros(val):
    while len(val) != 8:
        val = '0' + str(val)
    return val