from django.shortcuts import render, HttpResponse, redirect
from .models import Books

def homepage(request):
    return render(request, "books.html")

def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def add_book(request):
    form = request.POST
    title = form["books_title"]
    subtitle = form["books_subtitle"]
    description = form["books_description"]
    price = form["books_price"]
    genre = form["books_genre"]
    author = form["books_author"]
    year = form["books_year"]
    fields = Books(title=title, 
                    subtitle=subtitle, 
                    description=description,
                    price=price,
                    genre=genre,
                    author=author,
                    year=year)
    fields.save()
    return redirect(books)

def delete_book(request, id):
    deleted = Books.objects.get(id=id)
    deleted.delete()
    return redirect(books)

def mark_book(request, id):
    marked_book = Books.objects.get(id=id)
    marked_book.is_favorites = not marked_book.is_favorites
    marked_book.save()
    return redirect(books)

def BooksDetail(request, id):
    text = Books.objects.get(id=id)
    return render(request, "books_detail.html", {"books": text})