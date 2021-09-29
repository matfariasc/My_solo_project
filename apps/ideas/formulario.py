from .models import Ideas
from django import forms

class FormGenerico(forms.ModelForm):
    class Meta:
        model = Ideas
        # fields = "__all__"
        fields = ["title", "desc"]

        labels = {
            "title" : "Titulo",
            "desc" : "Descripcion",
        }
