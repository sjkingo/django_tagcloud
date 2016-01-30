from django import template
from math import log10

register = template.Library()

def compute_tag_sizes(tags, min_font_size, max_font_size):
    """
    This computes and returns a list of tag font weight sizes, between the
    minimum and maximum font sizes specified, using a logarthmic assessment.
    """
    tag_list = []
    max_weight = max([weight for _, weight in tags])
    for tag, weight in tags:
        if weight <= 0:
            size = min_font_size
        else:
            size_float = log10(weight) / log10(max_weight) * (max_font_size - min_font_size) + min_font_size
            size = int(round(size_float))
        tag_list.append((tag, '%spx' % size))
    return tag_list

@register.inclusion_tag('tagcloud/tagcloud.html')
def tagcloud(tags, min_font_size=12, max_font_size=38):
    """
    Generate a tagcloud from a list of (tag, weight) tuples. For instance:
    [('apple', 3), ('orange', '4'), ('pear', 9)]
    """
    tag_list = compute_tag_sizes(tags, min_font_size, max_font_size)
    return {'tag_list': tag_list}
