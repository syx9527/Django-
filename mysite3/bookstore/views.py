from django.shortcuts import *
from .models import Book


# Create your views here.

def all_book(request):
    all_book = Book.objects.filter(is_active=True)

    return render(request, "bookstore/all_book.html", locals())


def update_book(request, book_id):
    # book/update_book/2021001
    try:
        book = Book.objects.get(book_id=book_id, is_active=True)
    except Exception as e:
        print('--update book error is %s' % e)
        return HttpResponse('--The Book is not existed')

    if request.method == "GET":
        return render(request, 'bookstore/update_book.html', locals())

    if request.method == 'POST':
        price = request.POST['price']
        market_price = request.POST['market_price']
        book.book_price = price
        book.book_market_price = market_price
        book.save()

        return redirect('/book/all_book/')


def delete_book(request):
    # book/delete_book/2021001/
    book_id = request.GET.get('book_id')
    try:
        book = Book.objects.get(book_id=book_id, is_active=True)
        book.is_active = False
        book.save()
        return redirect('/book/all_book/')
    except Exception as e:
        print('--update book error is %s' % e)
        return HttpResponse('--The Book is not existed')
