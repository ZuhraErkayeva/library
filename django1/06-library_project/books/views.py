from django.shortcuts import render

from django.shortcuts import HttpResponse
from .models import *


def home_view(request):
    books = Book.objects.all()
    response = ""
    for book in books:
        response += f"""
            <h1>{book.title}</h1>
        """
        response += f"""
            <ul>
                <li>{book.description}</li>
                <li>{book.created_at}</li>
                <li>{book.updated_at}</li>
            </ul>
"""
    return HttpResponse(response)


def author_view(request):
    author = Author.objects.all()
    response = ""
    for authors in author:
        response += f"""
            <h1>{authors.first_name} {authors.last_name}</h1>
        """
        response += f"""
            <ul>
                <li>{authors.first_name}</li>
                <li>{authors.last_name}</li>
                <li>{authors.created_at}</li>
                <li>{authors.updated_at}</li>
            </ul>
"""
    return HttpResponse(response)


def category_view(request):
    categories = Categories.objects.all()
    response = ""
    for category in categories:
        response += f"""
            <h1>{category.name}</h1>
        """
        response += f"""
            <ul>
                <li>{category.name}</li>
                <li>{category.created_at}</li>
                <li>{category.updated_at}</li>
            </ul>
"""
    return HttpResponse(response)
