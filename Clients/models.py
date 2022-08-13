from django.db import models
from django.contrib.auth.models import User

class ClientsUserProfile(models.Model): 
    MASCULINE = "M"
    FÉMININE = "F"
    
    GENDER = [
        (MASCULINE , 'Masculine'),
        (FÉMININE , 'Féminine'),  
    ]
      
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER, max_length=255)
    adresse = models.CharField(max_length=255, blank= False)
    adresse2 = models.CharField(max_length=255, blank=True)
    adresse3 = models.CharField(max_length=255, blank=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.first_name
    


