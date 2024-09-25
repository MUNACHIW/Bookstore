from django.urls import path

from .views import CreateProfileView, ProfilesView


urlpatterns = [
    path("", CreateProfileView.as_view()),
    path("list", ProfilesView.as_view()),
]
