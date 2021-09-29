from django.urls import path
from .views import CrearUsuario, Detalles, Actulizar, Eliminar, ListaUsuarios

urlpatterns = [
    # path('registro', views.registro , name= "registro"),
    path('usuario', ListaUsuarios.as_view(), name = "usuarios" ),
    path("registro", CrearUsuario.as_view() , name="registro"),
    path("detalles/<int:pk>", Detalles.as_view() , name="detalles"),
    path("actulizar/<int:pk>", Actulizar.as_view() , name="actulizar"),
    path("eliminar/<int:pk>", Eliminar.as_view() , name="eliminar")

]