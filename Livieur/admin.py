from django.contrib import admin
from .models import LivreurUserProfile

@admin.register(LivreurUserProfile)
class User_Profile(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number", 
        "gender", 
        "adresse",
        "transport",
        "latitude",
        "longitude",
        "immatriculation"
    )
    

