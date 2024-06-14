from django.shortcuts import render
from .models import Author, Quote


def home(request):
    return render(request, "home.html")


def authors(request):
    all_authors = Author.objects.all()
    return render(request, "authors.html", {'authors': all_authors})


def quotes(request):
    all_quotes = Quote.objects.all()
    return render(request, "quotes.html", {'quotes': all_quotes})
