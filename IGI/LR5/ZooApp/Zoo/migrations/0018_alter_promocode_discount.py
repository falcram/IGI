# Generated by Django 5.0.6 on 2024-06-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0017_alter_ticket_promocode_alter_ticket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='discount',
            field=models.FloatField(),
        ),
    ]
