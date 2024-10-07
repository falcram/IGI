# Generated by Django 5.0.6 on 2024-10-04 11:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0023_article_date_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='Zoo.cartitem')),
            ],
        ),
        migrations.CreateModel(
            name='TicketDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('available_quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date_of_visit',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='is_canceled',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='promocode',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AddField(
            model_name='ticket',
            name='max_quantity',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='ticket',
            name='name',
            field=models.CharField(default='Билет на посещение зоопарка', max_length=100),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Zoo.promocode'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticketdate',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zoo.ticket'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='ticket_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zoo.ticketdate'),
        ),
    ]
