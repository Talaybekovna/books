from django.shortcuts import render, HttpResponse, redirect
from .models import Books

def homepage(request):
    return render(request, "books.html")

def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def add_books(request):
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

def delete(request, id):
    delete_book = Books.objects.get(id=id)
    delete_book.delete()
    return redirect(books)

def mark(request, id):
    mark_book = Books.objects.get(id=id)
    mark_book.is_favorites =True
    mark_book.save()
    return redirect(books)

def detail(request, id):
    books_list = Books.objects.all()
    book_detail = Books.objects.get(id=id)
    book_detail.save()
    return render(request, "books_detail.html", {"books_list": books_list})
    