from django.db import models

# Create your models here.
class Contact(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.nom