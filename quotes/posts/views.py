from django.shortcuts import render, redirect
from .models import Author, Quote


def home(request):
    return render(request, "home.html")


def authors(request):
    all_authors = Author.objects.all()
    return render(request, "authors.html", {'authors': all_authors})


def quotes(request):
    all_quotes = Quote.objects.all()
    return render(request, "quotes.html", {'quotes': all_quotes})


def add_quote(request):
    if request.method == 'POST':
        new_quote = request.POST.get('quoteText')
        author_id = request.POST.get('authorId')
        quote = Quote()
        quote.content = new_quote
        author = Author.objects.get(pk=author_id)
        quote.author = author
        quote.save()
        return redirect("/quotes")
    else:
        all_authors = Author.objects.all()
        return render(request, "add_quote.html", {'authors': all_authors})
