# Generated by Django 4.0.3 on 2022-03-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_restaurant_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
