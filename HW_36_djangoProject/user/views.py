from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user.models import User


def user_view(request):
    # data = list(User.objects.all().values())
    return JsonResponse(list(User.objects.all().values()), safe=False)