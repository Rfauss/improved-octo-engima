from django.contrib import admin
from .models import Recipe, Pantry

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Pantry)
