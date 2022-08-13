from django.db import models
from django.contrib.auth.models import User
from Clients.models import ClientsUserProfile

class VendeurUserProfile(models.Model): 
    MASCULINE = "M"
    FÉMININE = "F"
    
    GENDER = [
        (MASCULINE , 'Masculine'),
        (FÉMININE , 'Féminine'),  
    ]
      
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER, max_length=255)
    adresse = models.CharField(max_length=255)
    adresse2 = models.CharField(max_length=255, blank=True)
    adresse3 = models.CharField(max_length=255, blank=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.first_name

    
class DestinationColis(models.Model):
    Addresse = models.CharField(max_length=255) 
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=255 , blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.Addresse
      
class Colis(models.Model):
    code_secret =models.CharField(max_length=10000, default='', blank=True)
    vendeur = models.ForeignKey(VendeurUserProfile, on_delete=models.CASCADE, related_name="colois_vendeur")
    destination_colis = models.ForeignKey(DestinationColis, on_delete=models.CASCADE , related_name="colois_location_colis")
    name = models.CharField(max_length=255) 
    prix = models.DecimalField(max_digits=6, decimal_places=3)
    quantity = models.PositiveIntegerField()
    description = models.TextField(max_length=255 , blank=True)
    update_colis = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def generate_secret(self):
        self.secret = str(random.randint(10000, 99999))
    
    def __str__(self) -> str:
        return self.vendeur.user.first_name
    
   
    
class Paiement(models.Model): 
    vendeur = models.ForeignKey(VendeurUserProfile, on_delete=models.CASCADE, related_name="paiement_vendeur")
    colis = models.ForeignKey(Colis, on_delete=models.CASCADE, related_name="paiement_colis")
    destination_colis = models.ForeignKey(DestinationColis, on_delete=models.CASCADE , related_name="paiement_destination_colis")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.vendeur.user.first_name
