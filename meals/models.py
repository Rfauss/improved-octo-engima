from django.db import models
from django.conf import settings
from django.urls import reverse
from recipes.models import Recipe

from datetime import date

# Create your models here.


class Meals(models.Model):
    name = models.CharField(max_length=255, default="none")
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default="none")
    category = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk) + "_" + self.name


class MealPlan(models.Model):
    User = settings.AUTH_USER_MODEL
    title = models.CharField(max_length=128)
    currentDate = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(
        User,
        related_name="MealUser",
        on_delete=models.CASCADE,
        primary_key=True,
    )

    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + "_" + self.title

    def get_absolute_url(self):
        return reverse("meal_plan", kwargs={"pk": self.pk})
