from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from book.models import Book

def book_view(request):
    return JsonResponse(list(Book.objects.all().values()), safe=False)