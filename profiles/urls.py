from django.urls import path

from .views import CreateProfileView

urlpatterns = [path("", CreateProfileView.as_view())]
