from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from .forms import WhatBookForm
from .models import Book

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
class BookListView(ListView):
    model = Book

    def get_queryset(self, *args, **kwargs):
        context = super(BookListView, self).get_queryset(**kwargs)
        print(context)
        return context

class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        print(context)
        return context

class BookAddView(CreateView):
    model = Book
    success_url = "/view"
    fields = [
        "title",
        "author",
        "page_count",
        "publish_date",
        "ISBN_number",
    ]

def update_what_view(request):
    print (request)
    form = WhatBookForm(request.POST or None)

    if form.is_valid():
        ISBN_number = form.cleaned_data.get('ISBN_number')
        return HttpResponseRedirect(reverse('book_update_view', args = [ISBN_number]))

    template = 'update_what.html'
    context = {
        'form': form
    }
    return render(request, template, context)

class BookUpdateView(UpdateView):
    model = Book
    success_url = "/view"
    fields = [
        "title",
        "author",
        "page_count",
        "publish_date",
        "ISBN_number",
    ]

def remove_what_view(request):
    print (request)
    form = WhatBookForm(request.POST or None)

    if form.is_valid():
        ISBN_number = form.cleaned_data.get('ISBN_number')
        return HttpResponseRedirect(reverse('book_remove_view', args = [ISBN_number]))

    template = 'remove_what.html'
    context = {
        'form': form
    }
    return render(request, template, context)

class BookRemoveView(DeleteView):
    model = Book
    success_url = "/view"
