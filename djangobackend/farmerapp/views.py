from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Listing
from django.forms.models import model_to_dict

@api_view(['GET'])
def home(request):
    print(request.session['farmer']['id'])
    return JsonResponse({'info': 'Farmers App Home'})



@api_view(['POST'])
def addCrop(request):
    if request.method == 'POST':
        crop_name=request.data.get('crop_name')
        category=request.data.get('category')
        description=request.data.get('description')
        quantity=request.data.get('quantity')
        unit=request.data.get('unit')
        price_per_unit=request.data.get('price_per_unit')
        negotiable=request.data.get('negotiable')
        bulk_discount=request.data.get('bulk_discount')
        approx_maturity_date=request.data.get('approx_maturity_date')
        expected_harvest_date=request.data.get('expected_harvest_date')
        harvest_method=request.data.get('harvest_method')
        certifications=request.data.get('certifications')
        certified_by=request.data.get('certified_by')
        certification_id=request.data.get('certification_id')
        certification_validity=request.data.get('certification_validity')
        storage_condition=request.data.get('storage_condition')
        packaging_type=request.data.get('packaging_type')
        shelf_life=request.data.get('shelf_life')
        location=request.data.get('location')
        image=request.data.get('image')
        # delivery_available=request.data.get('delivery_available')
        farmer_id=request.session['farmer']['id']
        listing = Listing(crop_name=crop_name, category=category, description=description, quantity=quantity, unit=unit, price_per_unit=price_per_unit, negotiable=negotiable, bulk_discount=bulk_discount, approx_maturity_date=approx_maturity_date, expected_harvest_date=expected_harvest_date, harvest_method=harvest_method, certifications=certifications, certified_by=certified_by, certification_id=certification_id, certification_validity=certification_validity, storage_condition=storage_condition, packaging_type=packaging_type, shelf_life=shelf_life, location=location, image=image, farmer_id=farmer_id)
        listing.save()
        return JsonResponse({'info': 'Listed Crop'})
    else:
        return JsonResponse({'info': 'error Listing Crop'})
    # return JsonResponse({'info': 'Add Crop'})


def deleteCrop(request):
    if request.method == 'POST':
        crop_id = request.data.get('crop_id')
        listing = Listing.objects.get(id=crop_id)
        listing.delete()
        return JsonResponse({'info': 'Deleted Crop'})
    else:
        return JsonResponse({'info': 'error Deleting Crop'})
    # return JsonResponse({'info': 'Delete Crop'})

def updateCrop(request):
    if request.method == 'POST':
        crop_id = request.data.get('crop_id')
        crop_name=request.data.get('crop_name')
        category=request.data.get('category')
        description=request.data.get('description')
        quantity=request.data.get('quantity')
        unit=request.data.get('unit')
        price_per_unit=request.data.get('price_per_unit')
        negotiable=request.data.get('negotiable')
        bulk_discount=request.data.get('bulk_discount')
        approx_maturity_date=request.data.get('approx_maturity_date')
        expected_harvest_date=request.data.get('expected_harvest_date')
        harvest_method=request.data.get('harvest_method')
        certifications=request.data.get('certifications')
        certified_by=request.data.get('certified_by')
        certification_id=request.data.get('certification_id')
        certification_validity=request.data.get('certification_validity')
        storage_condition=request.data.get('storage_condition')
        packaging_type=request.data.get('packaging_type')
        shelf_life=request.data.get('shelf_life')
        location=request.data.get('location')        
        image=request.data.get('image')
        farmer_id=request.session['farmer']['id']

        listing = Listing.objects.get(id=crop_id)
        listing.crop_name=crop_name
        listing.category=category
        listing.description=description
        listing.quantity=quantity
        listing.unit=unit
        listing.price_per_unit=price_per_unit
        listing.negotiable=negotiable
        listing.bulk_discount=bulk_discount
        listing.approx_maturity_date=approx_maturity_date
        listing.expected_harvest_date=expected_harvest_date
        listing.harvest_method=harvest_method
        listing.certifications=certifications
        listing.certified_by=certified_by
        listing.certification_id=certification_id
        listing.certification_validity=certification_validity
        listing.storage_condition=storage_condition
        listing.packaging_type=packaging_type
        listing.shelf_life=shelf_life
        listing.location=location
        listing.image=image
        listing.farmer_id=farmer_id 

        listing.save()
        return JsonResponse({'info': 'Updated Crop'})
    else:    
        return JsonResponse({'info': 'error Updating Crop'})
    

def getCrop(request):
    if request.method == 'GET':
        crop_id = request.data.get('crop_id')
        listing = Listing.objects.get(id=crop_id)
        listing_dict = model_to_dict(listing)
        return JsonResponse(listing_dict)
    else:
        return JsonResponse({'info': 'error Getting Crop'})
    # return JsonResponse({'info': 'Get Crop'})