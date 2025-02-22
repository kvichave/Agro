from django.db import models
from userauth.models import Farmer


# Create your models here.


class Listing(models.Model):
    id = models.AutoField(primary_key=True)  # ✅ Fixed
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=100,null=False)
    category = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(default=0)  # ✅ Fixed
    units = models.IntegerField(max_length=50,default=0)  # ❌ Fixed (Changed from ImageField)
    price_per_unit = models.IntegerField(null=True, blank=True)
    negotiable = models.BooleanField(null=True, blank=True)
    bulk_discount = models.IntegerField(null=True, blank=True)
    approx_maturity_date = models.DateField(null=True, blank=True)
    expected_harvest_date = models.DateField(null=True, blank=True)
    harvest_method = models.CharField(max_length=100, null=True, blank=True)
    certifications = models.CharField(max_length=100, null=True, blank=True)
    certified_by = models.CharField(max_length=100, null=True, blank=True)
    certification_id = models.CharField(max_length=100, null=True, blank=True)
    certification_validity = models.DateField(null=True, blank=True)
    storage_condition = models.CharField(max_length=100, null=True, blank=True)
    packaging_type = models.CharField(max_length=100, null=True, blank=True)
    shelf_life = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    # def __str__(self):
    #     return f"{self.crop_name} - {self.quantity} {self.unit} (Farmer: {self.farmer_id.name})"
