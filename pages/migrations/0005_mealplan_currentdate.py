# Generated by Django 4.1.5 on 2023-01-24 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_remove_mealplan_currentdate"),
    ]

    operations = [
        migrations.AddField(
            model_name="mealplan",
            name="currentDate",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
