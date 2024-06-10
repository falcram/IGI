# Generated by Django 5.0.6 on 2024-06-04 17:50

import Zoo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0007_alter_kind_of_animal_countries_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(null=True, validators=[Zoo.models.User.validate_age]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, null=True, validators=[Zoo.models.User.validate_phone]),
        ),
    ]
