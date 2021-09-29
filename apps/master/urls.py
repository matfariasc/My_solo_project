from django.urls import path
from . import views
from .views import ListaIdeas

urlpatterns = [
    path('', views.index , name= "index"),
    path('dashboard', ListaIdeas.as_view(), name = "dashboard" )
]