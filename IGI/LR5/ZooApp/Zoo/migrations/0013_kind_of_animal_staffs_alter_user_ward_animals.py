# Generated by Django 5.0.6 on 2024-06-09 13:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0012_remove_kind_of_animal_staffs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kind_of_animal',
            name='staffs',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='ward_animals',
            field=models.ManyToManyField(blank=True, to='Zoo.kind_of_animal'),
        ),
    ]
