# Generated by Django 4.1.5 on 2023-01-26 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0009_remove_mealplan_owner_pantry_food_pantry_foodqty_and_more"),
        ("meals", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mealplan",
            name="content",
        ),
        migrations.RemoveField(
            model_name="mealplan",
            name="date",
        ),
        migrations.RemoveField(
            model_name="mealplan",
            name="recipe",
        ),
        migrations.CreateModel(
            name="Meals",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="none", max_length=255)),
                ("description", models.CharField(default="none", max_length=255)),
                ("category", models.CharField(max_length=100)),
                (
                    "recipe",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="recipes.recipe"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="mealplan",
            name="meal",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="meals.meals"
            ),
        ),
    ]