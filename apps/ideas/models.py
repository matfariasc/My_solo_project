from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Ideas(models.Model):
    title = models.CharField(max_length=225)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(Usuario,related_name="idea_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(Usuario,related_name="liked_ideas")
