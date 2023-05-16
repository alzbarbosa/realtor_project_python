from django.db import models
from django.contrib.auth.models import User

PROPERTY_TYPE = (
    ("house", "House"),
    ("apartment", "Apartment"),
    ("commercial", "Commercial"),
    ("mansion", "Mansion")
)

STATUS = (
    (0, "Available"),
    (1, "Sold")
)

# Create your models here.
class Item(models.Model):
    property = models.CharField(max_length=1000, unique=True)
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE)
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    bedrooms = models.IntegerField(default=0)
    has_pool = models.BooleanField(default=False)
    has_garage = models.BooleanField(default=False)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    realtor = models.ForeignKey(User, on_delete=models.PROTECT)  #models.CASCADE || models.SET_NULL
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property

