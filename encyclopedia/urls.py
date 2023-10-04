from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:article>", views.entry, name="entry"),
    path("random", views.rand, name="random"),
    path("new", views.new, name="new"),
    path("wiki/edit/<str:article>", views.edit, name = "edit"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("search", views.search, name= "search"),
    ]
