from django.urls import path

from .views import *

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("edit/<int:pk>/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("delete/<int:pk>/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/", PantryDetailView.as_view(), name="pantry_detail"),
    path("edit/<int:pk>/", PantryUpdateView.as_view(), name="pantry_edit"),
    path("delete/<int:pk>/", PantryDeleteView.as_view(), name="pantry_delete"),
    path("new/", PantryCreateView.as_view(), name="pantry_new"),
]
