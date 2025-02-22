from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Farmer
# Create your views here.
from django.forms.models import model_to_dict

@api_view(['POST', 'GET'])
def signup(request):

    if request.method == 'GET':
        return Response({'message': 'Farmer get request'})
    if request.method == 'POST':
        # print(request.data["name"])
        category = request.data["category"]
        name = request.data["name"]
        email = request.data["email"]
        password = request.data["password"]
        phone = request.data["phone"]
        location = request.data["location"]
        if category == 'farmer':
            farmer = Farmer(name=name, email=email, password=password, phone=phone,location=location)
            farmer.save()
            farmer_dict = model_to_dict(farmer)
            request.session['farmer'] = farmer_dict
            print(request.session['farmer']) #request.session['farmer'].name
            print(request.session['farmer']['id']) #request.session['farmer'].name
            print("id: ", farmer.id) #farmer.id
            return Response({'message': 'Farmer created'})
        else:
            return Response({'message': 'Invalid category'})
        
        # return Response({'message': 'Farmer created'})



def login(request):
    if request.method == 'GET':

        return Response({'message': 'Farmer get request'})
    if request.method == 'POST':
        email = request.data["email"]
        password = request.data["password"]
        farmer = Farmer.objects.filter(email=email, password=password).first()
        
        if farmer:
            farmer_dict = model_to_dict(farmer)
            print("farmer_dict: ",farmer_dict)
            request.session['farmer'] = farmer_dict
            return Response({'message': 'Farmer logged in'})
        else:
            return Response({'message': 'Invalid farmer'})