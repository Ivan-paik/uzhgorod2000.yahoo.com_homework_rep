from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from purchase.models import Purchase

def purchase_view(request):
    return JsonResponse(list(Purchase.objects.all().values()), safe=False)
