from django.contrib import admin
from .models import ClientsUserProfile

@admin.register(ClientsUserProfile)
class User_Profile(admin.ModelAdmin):
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
                

# Register your models here.
