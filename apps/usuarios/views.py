from .models import Usuario
from .formulario import FormActulizar, FormRegistro
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.list import ListView


# Create your views here.

# def registro(request):
#     context = {
#         "form" : FormRegistro()
#     }
#     return render (request, "usuarios.html", context)



class CrearUsuario(CreateView):
    template_name = "registro.html"
    form_class = FormRegistro
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        usuario = form.save(commit = False)
        usuario.set_password(usuario.password)
        usuario.username = usuario.email
        usuario.save()
        login(self.request, usuario)
        return super().form_valid(form)

class ListaUsuarios(ListView):
    model = Usuario
    template_name = "usuarios.html"
    paginate_by = 10

class Detalles(DetailView):
    model = Usuario
    template_name = "detalles.html"

class Actulizar(UpdateView):
    model = Usuario
    form_class = FormActulizar
    template_name = "editar.html"
    success_url = reverse_lazy("usuarios")

class Eliminar(DeleteView):
    model = Usuario
    success_url = reverse_lazy("usuarios")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)