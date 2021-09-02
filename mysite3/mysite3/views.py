from django.shortcuts import *


def test_static(request):
    # #
    return render(request, "test_static.html")


def test_index(request):
    return redirect('book/all_book/')
