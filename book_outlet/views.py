from django.shortcuts import render

# Create your views here.
from .models import Book


def index(request):
    Books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": Books})
