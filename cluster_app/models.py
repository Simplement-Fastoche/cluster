from django.db import models

# Create your models here.

class FichierFrom(models.Model):
     file= models.FileField()
     class Meta:
          db_table ="fichier"