from django.db import models
from django.contrib.auth.models import User, AbstractUser
from tzlocal import get_localzone_name
import re
import logging
import django.forms
from django.urls import reverse
from django.utils import timezone
from datetime import time
from datetime import timedelta

class User(AbstractUser):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    status_choices = (
        ("client","client"),
        ("staff","staff")
    )
    def validate_phone(value):
        phone_pattern = re.compile(r'\+375\((29|33|44|25)\)\d{7}')
        if not re.fullmatch(phone_pattern, str(value)):
            raise django.forms.ValidationError("Неверный формат номера телефона (правильный: +375(XX)XXXXXXX.")

    def validate_age(value):
        if value < 18 or value > 100:
            raise django.forms.ValidationError("Только для людей старше 18 лет.")
        
    status = models.CharField(choices=status_choices, default="client", max_length=6)
    age = models.PositiveSmallIntegerField(validators=[validate_age], null= True)
    phone = models.CharField(max_length=15, validators=[validate_phone], null= True)
    address = models.CharField(max_length=255, null= True)
    timezone = get_localzone_name()
    groups = None
    user_permissions = None
    job_t = models.ForeignKey('Job_title',on_delete=models.PROTECT, null= True, blank=True)
    ward_animals = models.ManyToManyField('kind_of_animal',blank=True)
    
    def __str__(self):
        return self.first_name
    

class Animal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Animal Name")
    image = models.ImageField(upload_to='images/', null=True)
    kind = models.ForeignKey('kind_of_animal',on_delete=models.PROTECT, null= True)
    def __str__(self):
        return self.name

class kind_of_animal(models.Model):
    kind_name = models.CharField(max_length=255, verbose_name="Animal Kind Name", unique=True, null= True)
    family = models.ForeignKey('family',on_delete=models.PROTECT, null= True)
    feed = models.ForeignKey('feed',on_delete=models.PROTECT, null= True)
    countries = models.ManyToManyField('Country_of_residence')
    av = models.OneToOneField('Aviary',on_delete=models.SET_NULL, null=True)
    staffs = models.ManyToManyField('User', blank=True)
    def __str__(self):
        return self.kind_name

class family(models.Model):
    family_name = models.CharField(max_length=255, verbose_name="Animal Family Name", unique=True)
    def __str__(self):
        return self.family_name

class feed(models.Model):
    feed_name = models.CharField(max_length=255, verbose_name=" feed_name", null = True)
    amount_kg = models.FloatField(verbose_name="Вес (кг)", null = True)
    reciept_date = models.DateTimeField(null = True)
    expiration_date = models.DateTimeField( null= True)
    def __str__(self):
        return self.feed_name

class Country_of_residence(models.Model):
    county = models.CharField(max_length=255, verbose_name=" feed_name", null = True)
    def __str__(self):
        return self.county

class Aviary(models.Model):
    aviary_number = models.IntegerField(unique=True, null=True)
    aviary_name = models.CharField(max_length=100, verbose_name="aviary_name", null = True)
    basin = models.BooleanField(default=False)
    size_in_square_meters = models.FloatField(null=True)
    def __str__(self):
        return self.aviary_name

class Job_title(models.Model):
    j_title = models.CharField(max_length=100,null=True, verbose_name='job title') 
    def __str__(self):
        return self.j_title

class CompanyInfo(models.Model):
    def validate_phone(value):
        phone_pattern = re.compile(r'\+375\((29|33|44|25)\)\d{7}')
        if not re.fullmatch(phone_pattern, str(value)):
            raise django.forms.ValidationError("Неверный формат номера телефона (правильный: +375(XX)XXXXXXX.")
    zooname = models.CharField(max_length=25, verbose_name="Zoo Name", null = True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, validators=[validate_phone], null = True)
    text = models.TextField()
    logo = models.ImageField(upload_to='images/', null = True)

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date = models.DateField(auto_now_add=True)

class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    need = models.TextField()

class Review(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)

class Contact(models.Model):
    description = models.TextField()
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')

class UsedDiscounts(models.Model):
    promocode = models.ForeignKey('Promocode', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/') 
    website = models.URLField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    

# Модель билета
class Ticket(models.Model):
    name = models.CharField(max_length=100, default="Билет на посещение зоопарка")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=100.00)  # Цена билета
    max_quantity = models.PositiveIntegerField(default=100)  # Максимальное количество билетов на дату

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Сохраняем билет
        super().save(*args, **kwargs)
        
        # После сохранения создаем даты для доступных билетов на ближайшие 30 дней
        for i in range(30):
            date = timezone.now().date() + timedelta(days=i)
            # Создаем запись о билетах на конкретную дату, если она еще не существует
            TicketDate.objects.get_or_create(
                ticket=self, 
                date=date, 
                defaults={'available_quantity': self.max_quantity}
            )


# Модель билетов для конкретных дат
class TicketDate(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)  # Связь с моделью билета
    date = models.DateField()  # Дата посещения
    available_quantity = models.PositiveIntegerField()  # Доступное количество билетов на дату

    def __str__(self):
        return f"Билеты на {self.date}: осталось {self.available_quantity} из {self.ticket.max_quantity}"


# Модель элементов корзины
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
    ticket_date = models.ForeignKey(TicketDate, on_delete=models.CASCADE)  # Связанная дата билета
    quantity = models.PositiveIntegerField(default=0)  # Количество билетов в корзине

    def __str__(self):
        return f"{self.quantity} билетов на {self.ticket_date.date}"


# Модель промокода для скидок

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)  # Промокод
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Скидка в процентах

    def __str__(self):
        return f"Промокод {self.code} со скидкой {self.discount}%"


# Модель заказа
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    promo_code = models.ForeignKey(PromoCode, null=True, blank=True, on_delete=models.SET_NULL)  # Промокод
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def get_total_cost(self):
        total = sum(item.ticket_date.ticket.price * item.quantity for item in self.items.all())
        if self.promo_code:
            total = total - (total * (self.promo_code.discount / 100))
        return total
