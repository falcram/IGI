# Generated by Django 5.0.6 on 2024-06-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0002_animal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('logo', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
