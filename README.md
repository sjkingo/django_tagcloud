# django_tagcloud

A simple Django templatetag for generating a [tagcloud](https://en.wikipedia.org/wiki/Tag_cloud).

[![PyPI](https://img.shields.io/pypi/v/nine.svg)](https://pypi.python.org/pypi/django_tagcloud)

## How to use

Installation and usage is simple:

1. `$ pip install django_tagcloud`

2. Add `tagcloud` to your `INSTALLED_APPS`

3. In your view code, assemble a list of `(tag, weight)` tuples and add it to the response context, for instance:

   ```python
   ...
   tag_list = [('apple', 3), ('orange', 9), ('pear', 4), ('plum', 12)]
   return render(request, template, {'tag_list': tag_list})
   ```

4. In a template, simply call the templatetag:

   ```django
   {% load tagcloud %}

   {% tagcloud tag_list %}
   ```

## Customisation

Currently the only customisation possible is specifying the minimum and maximum
font sizes that the templatetag will use. By default these are 12px and 38px.
You can change this by passing one (or both) as arguments to the templatetag:

```django
{% tagcloud tag_list 18 32 %}
```
