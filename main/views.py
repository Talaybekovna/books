from django.shortcuts import render, HttpResponse, redirect
from .models import Books

def homepage(request):
    return render(request, "books.html")

def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})
