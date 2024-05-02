from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class Clients(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    username = models.CharField(max_length=12)
    email = models.CharField(max_length=20, default=True)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Clients'


    def __str__(self):
        return f"{self.username}"



class Plants(models.Model):
    LOCATIONS = (('Budalangi','Budalangi'),('Bulemia','Bulemia'),('Port_victoria','PortVictoria'),('Busia','Busia'),('Mubwayo', 'Mubwayo'),('Rongo', 'Rongo'),('Mundika', 'Mundika'),('Igigo','Igigo'),('Sirimba','Sirimba'),)
    username = models.CharField(max_length=15)
    farm_no = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=20, choices=LOCATIONS, default='Budalangi')
    farm_image = models.ImageField(upload_to= 'media/')
    class Meta:
        verbose_name_plural = 'Plants'

    def __str__(self):
        return f"{self.username}"

class Treatment(models.Model):
    phone_no = models.PositiveIntegerField()
    disease_image = models.ImageField(upload_to = 'media/')
    Description = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.phone_no}"


class Products(models.Model):
    LOCATIONS = (('Budalangi','Budalangi'),('Bulemia','Bulemia'),('Port_victoria','PortVictoria'),('Busia','Busia'),('Kisumu', 'Kisumu'),('Rongo', 'Rongo'),('Migori', 'Migori'),('Igigo','Igigo'),('Sirimba','Sirimba'),)
    username = models.CharField(max_length=30)
    phone_no = models.PositiveIntegerField()
    Product_name = models.CharField(max_length=20)
    Product_Image = models.ImageField(upload_to = 'media/products')
    location = models.CharField(max_length=20, choices=LOCATIONS, default='Budalangi')

    class Meta:
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return f"{self.username}"


class Medicines(models.Model):
    drug_used = models.CharField(max_length=15, default= 'Pentagon')
    type = models.CharField(max_length=10, default="Insecticide")
    quantity = models.CharField(max_length = 15, default= str("1 ") +' ml' )
    treatmentDate = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Medicines'
        
    def __str__(self):
        return f"{self.drug_used}"




