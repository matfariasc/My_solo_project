from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    fecha_nacimiento = models.DateField()
    updated_at = models.DateField(auto_now=True)