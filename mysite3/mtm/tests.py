from django.test import TestCase

# Create your tests here.
from .models import *

b1 = Book.objects.all()
# b2 = Book.objects.filter()
for i in b1:
    print(i.author.all())

a1 = Author.objects.all()

for i in a1:
    print(i.book_set.filter())
