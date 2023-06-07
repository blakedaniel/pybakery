# Generated by Django 4.2 on 2023-04-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pybakery", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipes",
            name="image",
            field=models.ImageField(default={}, upload_to=""),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="ingredients",
            unique_together={("recipe", "ingredient")},
        ),
    ]
