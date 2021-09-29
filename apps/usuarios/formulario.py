from .models import Usuario
from django import forms

class FormGenerico(forms.ModelForm):
    class Meta:
        model = Usuario
        # fields = "__all__"
        fields = ["first_name", "last_name","fecha_nacimiento", "email"]

        labels = {
            "first_name" : "Nombre",
            "last_name" : "Apellido",
            "fecha_nacimiento" : "Fecha nacimiento",
            "email" : "Email"
        }

        widgets = {
            "fecha_nacimiento" : forms.DateInput(
                attrs= {
                    "type": "Date"
                }
            )
        }

class FormRegistro(FormGenerico):
    password =forms.CharField(max_length= 100)
    confirmar_password = forms.CharField(max_length=100, label = "Confirmar")

class FormActulizar(FormGenerico):
    pass