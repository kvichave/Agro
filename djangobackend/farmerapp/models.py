from django.db import models
from userauth.models import Farmer


# Create your models here.


class Listing(models.Model) :
    crop_id=models.AutoField(primary_key=True),
    farmer_id=models.ForeignKey(Farmer,on_delete=models.CASCADE),
    crop_name=models.CharField(max_length=100),
    category=models.CharField(max_length=100),
    description=models.CharField(max_length=100),
    quantity=models.IntegerField(),
    unit=models.ImageField(max_length=100),
    price_per_unit=models.IntegerField(),
    negotiable=models.BooleanField(),
    bulk_discount=models.IntegerField(),
    approx_maturity_date=models.DateField(max_length=100),
    expected_harvest_date=models.DateField(),
    harvest_method=models.CharField(max_length=100),
    certifications=models.CharField(max_length=100),
    certified_by=models.CharField(max_length=100),
    certification_id=models.CharField(max_length=100),
    certification_validity=models.DateField(),
    storage_condition=models.CharField(max_length=100),
    packaging_type=models.CharField(max_length=100),
    shelf_life=models.IntegerField(),
    location=models.CharField(max_length=100),
    # delivery_available=models.BooleanField(),
    image=models.ImageField(upload_to='images/'),
