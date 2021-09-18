from django.test import TestCase

# Create your tests here.
from django.core.cache import cache

cache.set('uuname', 'syx', 20)
print(cache.get("uuname"))
