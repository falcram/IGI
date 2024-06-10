from django.db import models
from django.contrib.auth.models import User, AbstractUser
from tzlocal import get_localzone_name
import re
import logging
import django.forms
from django.urls import reverse
from django.utils import timezone
from datetime import time


class User(AbstractUser):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = (
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
        
    status = models.CharField(choices=status, default="client", max_length=6)
    age = models.PositiveSmallIntegerField(validators=[validate_age], null= True)
    phone = models.CharField(max_length=15, validators=[validate_phone], null= True)
    address = models.CharField(max_length=255, null= True)
    timezone = get_localzone_name()
    groups = None
    user_permissions = None
    job_t = models.ForeignKey('Job_title',on_delete=models.PROTECT, null= True, blank=True)
    ward_animals = models.ManyToManyField('kind_of_animal',blank=True)
    
    # def save(self, *args, **kwargs):
    #     phone_pattern = re.compile(r'\+375\((29|33|44|25)\)\d{7}')
    #     if not re.fullmatch(phone_pattern, str(self.phone)) or self.age < 18 or self.age > 100:

    #         logging.exception(f"ValidationError, {self.phone} is in incorrect format OR 18 < {self.age} < 100")

    #         raise django.forms.ValidationError("Error while creating user (Check phone number and age!)")
    #     super().save(*args, **kwargs)

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
    
class News(models.Model):
    title = models.TextField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)

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

class Promocode(models.Model):
    code = models.CharField(max_length=10)
    #discount = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.FloatField()
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

class Ticket(models.Model):
    user = models.ForeignKey('User', related_name='ticket',on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    date_of_visit = models.DateTimeField(null= True,auto_now_add=True)
    #promocode = models.CharField(max_length=10,  null= True, blank=True)
    promocode = models.ForeignKey('Promocode',related_name='ticket', null=True, blank=True, on_delete=models.SET_NULL)
    is_canceled = models.BooleanField(default=False)
    def use_discount(self, promocode):
        if UsedDiscounts.objects.filter(promocode_id=promocode, user_id=self.user).exists():
            return
        self.price *= (100 - promocode.discount) / 100
        self.save()
        UsedDiscounts.objects.create(promocode=promocode, user=self.user)


"""


class UsedDiscounts(models.Model):
    promocode = models.ForeignKey(Promocode, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date = models.DateField(auto_now_add=True)


class Contact(models.Model):
    description = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')



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
"""