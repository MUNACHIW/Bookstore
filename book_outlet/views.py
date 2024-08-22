from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Book
from django import template
from django.db.models import Avg, Max, Min


def index(request):
    Books = Book.objects.all().order_by("rating")
    numbooks = Books.count()
    avg_rating = Books.aggregate(Avg("rating"))
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": Books,
            "total_number_of_books": numbooks,
            "average_rating": avg_rating,
        },
    )


def book_detail(request, slug):

    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        },
    )
