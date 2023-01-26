from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import MealPlan


class MealPlanListView(ListView):
    model = MealPlan
    template_name = "meals/meal_plan.html"
