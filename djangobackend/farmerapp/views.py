from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Listing

@api_view(['GET'])
def home(request):
    request.data.get('crop_name')
    return JsonResponse({'info': 'Farmers App Home'})


def addCrop(request):
    if request.method == 'POST':
        crop_name=request.data.get('crop_name')
        category=request.data.get('category')
        return JsonResponse({'info': 'Add Crop'})
    else:
        return JsonResponse({'info': 'Add Crop'})
    # return JsonResponse({'info': 'Add Crop'})