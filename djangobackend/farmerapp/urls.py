from django.urls import path
from .views import *
urlpatterns = [
    path('farmer/', home),
    path('api/farmer/addCrop/', addCrop),

]
