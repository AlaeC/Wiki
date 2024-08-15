from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<url_name>/", views.find_page, name="entry"),
    path("random", views.random_page, name="random"),
    path("new_page", views.new_page, name="create new page"),
    path("search", views.search_page, name="search"),
    path("<str:url_name>/edit/", views.edit_entry, name="edit"),
]