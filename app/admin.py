from django.contrib import admin
from .models import Clients
from .models import Treatment, Products, Medicines, Plants

@admin.register(Treatment)
class TreatmentTable(admin.ModelAdmin):
    list_display = ['phone_no', 'Description']

@admin.register(Clients)
class ClientsTable(admin.ModelAdmin):
    list_display = ['username']

@admin.register(Products)
class ProductsTable(admin.ModelAdmin):
    list_display = ['username', 'phone_no', 'Product_name', 'location']
    
@admin.register(Medicines)
class MedicinesTable(admin.ModelAdmin):
    list_display = ['drug_used', 'type', 'quantity', 'treatmentDate']


@admin.register(Plants)
class PlantsTable(admin.ModelAdmin):
    list_display = ['username', 'farm_no', 'location']