# Generated by Django 4.1.5 on 2023-01-23 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_alter_recipe_ratings"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="ratings",
        ),
    ]
