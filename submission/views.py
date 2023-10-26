from django.http import JsonResponse
from django.shortcuts import render


def submit_an_animal(request):
    if request.method != 'POST':
        return JsonResponse({}, status=405)

    
