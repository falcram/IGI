# Generated by Django 5.0.6 on 2024-06-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0008_alter_user_address_alter_user_age_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
    ]
