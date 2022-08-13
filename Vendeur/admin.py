from django.contrib import admin
from .models import VendeurUserProfile, Colis, DestinationColis, Paiement

@admin.register(VendeurUserProfile)
class VendeurUserProfile(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number", 
        "gender", 
        "adresse",
        "adresse2",
        "adresse3",
        "latitude",
        "longitude"
        
)
    
@admin.register(Colis)
class Colis(admin.ModelAdmin):
    list_display = (
        "vendeur", 
        "destination_colis", 
        "name", 
        "prix", 
        "quantity", 
        "description", 
        "update_colis",
        "active"
)
    
@admin.register(DestinationColis)
class DestinationColis(admin.ModelAdmin):
    list_display = (
        "Addresse", 
        "prix", 
        "description",      
)
    
@admin.register(Paiement)
class Paiement(admin.ModelAdmin):
    list_display = (
        "vendeur", 
        "colis", 
        "destination_colis",         
)

# Register your models here.
