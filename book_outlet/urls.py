from django.urls import path


from . import views


urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.ReviewView.as_view(), name="book-detail"),
]
