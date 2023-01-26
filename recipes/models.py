from django.db import models
from django.urls import reverse
from django_project import settings

# Create your models here.
class Recipe(models.Model):
    User = settings.AUTH_USER_MODEL
    title = models.CharField(max_length=128)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # ratings = models.IntegerField(null=True)
    image = models.ImageField(upload_to="images/", default=None)
    owner = models.ForeignKey(
        User,
        related_name="User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})


class Pantry(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    food = models.CharField(max_length=255, default="none")
    spice = models.CharField(max_length=255, default="none")
    herb = models.CharField(max_length=255, default="none")
    foodQty = models.IntegerField(default=0)
    spiceQty = models.IntegerField(default=0)
    herbQty = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk) + "_" + self.title

    def get_absolute_url(self):
        return reverse("pantry_detail", kwargs={"pk": self.pk})
