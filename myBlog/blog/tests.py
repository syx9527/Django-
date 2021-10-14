from django.test import TestCase

# Create your tests here.
from .models import Article

a = Article.objects.values()
print(a)
