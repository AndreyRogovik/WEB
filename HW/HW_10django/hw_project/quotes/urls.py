from django.urls import path
from .views import author_detail  # Import the author_detail view
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="main"),
    path("<int:page>", views.main, name="root_paginate"),
    path('authors/<str:author_id>/', author_detail, name='author_detail'),  # Include the author_detail view
]
