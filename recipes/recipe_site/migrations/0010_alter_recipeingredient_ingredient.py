# Generated by Django 4.0.5 on 2022-06-23 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_site', '0009_alter_recipeingredient_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='recipes', to='recipe_site.ingredient'),
        ),
    ]
