from django.shortcuts import render
from django.views.generic.edit import CreateView
from .formulario import FormGenerico
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.

class CrearIdea(CreateView):
    template_name = "registro.html"
    form_class = FormGenerico
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        ideas = form.save(commit = False)
        ideas.uploaded_by = self.request.user
        ideas.save()
        return super().form_valid(form)