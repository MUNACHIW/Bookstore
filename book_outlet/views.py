from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views import View

# Create your views here.
from .models import Book Review
from django import template
from django.db.models import Avg, Max
from .forms import Reviewform
from django.urls import reverse
class ReviewView(View):
    def get(self,request ):
         form = ReviewForm()
          return render(
                request,
                "book_outlet/book_detail.html",
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "rating": book.rating,
                    "is_bestseller": book.is_bestselling,
                    "bookreview":book.reviews.all,
                    "form":form
                } 
    )
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.save()
            return HttpResponseRedirect(reverse('book-detail', args=[slug]))
        form = ReviewForm()
        return render(
                request,
                "book_outlet/book_detail.html",
                {
                    "form":form
                } 
         )

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


# def book_detail(request, slug):

#     # try:
#     #     book = Book.objects.get(pk=id)
#     # except:
#     #     Http404()
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             Review.save()
#             return HttpResponseRedirect(reverse('book-detail', args=[slug]))
#     else:
#         book = get_object_or_404(Book, slug=slug)
#         form = ReviewForm()
#     return render(
#         request,
#         "book_outlet/book_detail.html",
#         {
#             "id": book.id,
#             "title": book.title,
#             "author": book.author,
#             "rating": book.rating,
#             "is_bestseller": book.is_bestselling,
#             "bookreview":book.reviews.all,
#             "form":form
#         },
#     )
    
def UpdateReview(request, id):
    if request.method == 'POST':
           existing_data = book.review.get(pk=id)
           if existing_data:
                form = ReviewForm(request.POST, instance=existing_data)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('book-detail', args=[slug]))