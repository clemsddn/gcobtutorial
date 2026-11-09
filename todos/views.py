from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Tache
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class TacheListView(ListView):
    model = Tache
    template_name = 'todos/tache_list.html'
    context_object_name = 'taches'


class TacheDetailView(DetailView):
    model = Tache
    template_name = 'todos/tache_detail.html'


class TacheCreateView(SuccessMessageMixin, CreateView):
    model = Tache
    fields = ['titre', 'description', 'terminee']
    template_name = 'todos/tache_form.html'
    success_url = reverse_lazy('tache-list')
    success_message = "✅ Tâche « %(titre)s » créée avec succès !"


class TacheUpdateView(SuccessMessageMixin, UpdateView):
    model = Tache
    fields = ['titre', 'description', 'terminee']
    template_name = 'todos/tache_form.html'
    success_url = reverse_lazy('tache-list')
    success_message = "✏️ Tâche « %(titre)s » modifiée."


class TacheDeleteView(DeleteView):
    model = Tache
    template_name = 'todos/tache_confirm_delete.html'
    success_url = reverse_lazy('tache-list')

    def form_valid(self, form):
        messages.success(self.request, f"🗑️ Tâche « {self.object.titre} » supprimée.")
        return super().form_valid(form)