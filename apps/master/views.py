from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from apps.usuarios.models import Usuario
from apps.ideas.models import Ideas

# Create your views here.

def index(request):
    return render(request, "index.html")


@login_required()

def dashboard(request):
    return render(request, "dashboard.html")

class ListaIdeas(ListView):
    model = Ideas
    template_name = "dashboard.html"
    paginate_by = 10

