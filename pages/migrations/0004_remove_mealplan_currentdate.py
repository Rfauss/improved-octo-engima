# Generated by Django 4.1.5 on 2023-01-24 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_mealplan_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mealplan",
            name="currentDate",
        ),
    ]
