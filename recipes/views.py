from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
    TemplateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe, Pantry
from django.shortcuts import get_object_or_404

# Create your views here.


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe/recipe_new.html"
    fields = (
        "title",
        "content",
        "image",
    )

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = (
        "title",
        "content",
        "image",
    )
    template_name = "recipe/recipe_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "recipe/recipe_delete.html"
    success_url = reverse_lazy("recipe_list")

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class PantryListView(ListView):
    model = Pantry
    template_name = "pantry/pantry_view.html"


class PantryDetailView(DetailView):
    model = Pantry
    template_name = "pantry/pantry_detail.html"


class PantryCreateView(CreateView):
    model = Pantry
    template_name = "pantry/pantry_create.html"


class PantryUpdateView(UpdateView):
    model = Pantry
    template_name = "pantry/pantry_edit.html"


class PantryDeleteView(DeleteView):
    model = Pantry
    template_name = "pantry/pantry_delete.html"


# def delete_pantry(request, pantry_item):
#     pantry_item = get_object_or_404(
#         Pantry,
#     )
