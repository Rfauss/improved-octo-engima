from django.urls import path

from .views import MealPlanListView

urlpatterns = [
    path("", MealPlanListView.as_view(), name="meal_plan"),
]
