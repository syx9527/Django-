from django.shortcuts import *


# Create your views here.
def index(request):

    return render(request, 'index/index.html', {'request': request})
