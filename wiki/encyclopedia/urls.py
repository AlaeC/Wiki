from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<url_name>/", views.find_page, name="entry"),
    path("random", views.random_page, name="random")
]
