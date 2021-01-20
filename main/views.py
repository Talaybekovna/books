from django.shortcuts import render, HttpResponse, redirect

def homepage(request):
    return render(request, "books.html")
