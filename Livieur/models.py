from django.db import models
from django.contrib.auth.models import User

class LivreurUserProfile(models.Model): 
    MASCULINE = "M"
    FÉMININE = "F"
    
    VOITURE = "V"
    MOTOCYCLE = "M"
    VELO = "VL"
    
    GENDER = [
        (MASCULINE , 'Masculine'),
        (FÉMININE , 'Féminine'),  
    ]
    
    TYPE_TRANSPORT = [
        (VOITURE, 'Voiture'),
        (VELO, 'Velo'),
        (MOTOCYCLE, 'MOTOCYCLE')
    ]
    
      
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER, max_length=255)
    adresse = models.CharField(max_length=255)
    transport = models.CharField(choices=TYPE_TRANSPORT , max_length=255)
    immatriculation = models.CharField(max_length=255, blank=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.first_name



    
    
    

