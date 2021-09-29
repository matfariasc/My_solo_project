from django.urls import path
from .views import CrearIdea

urlpatterns = [
    path("newidea", CrearIdea.as_view() , name="crearidea"),
]
