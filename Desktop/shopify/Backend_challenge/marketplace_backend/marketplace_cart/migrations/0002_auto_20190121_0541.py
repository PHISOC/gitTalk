# Generated by Django 2.1.5 on 2019-01-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory_count',
            field=models.FloatField(),
        ),
    ]
