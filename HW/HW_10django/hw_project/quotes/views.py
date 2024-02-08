from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from .models import Author
# Create your views here.
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


# def author_detail(request, author_id):
#     db = get_mongodb()
#     authors = db.authors.find()
#     authors = db.authors.find_one({'_id': author_id})
#     return render(request, 'quotes/authors.html', context={'authors': authors, 'authors': authors})


class AuthorPageView(DetailView):
    template_name = 'authors-details.html'
    model = Author
    context_object_name = 'author'

