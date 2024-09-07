from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Animal)
admin.site.register(kind_of_animal)
admin.site.register(family)
admin.site.register(News)
admin.site.register(CompanyInfo)
admin.site.register(Promocode)
admin.site.register(FAQ)
admin.site.register(Vacancy)
admin.site.register(Review)
admin.site.register(feed)
admin.site.register(Country_of_residence)
admin.site.register(Aviary)
admin.site.register(Job_title)
admin.site.register(Contact)
admin.site.register(Ticket)
"""
admin.site.register(CompanyInfo)

<p>{{ company_info.zooname }}</p>
    <p>{{ company_info.email }}</p>
    <p>{{ company_info.phone }}</p>
    class CompanyInfo(models.Model):
    def validate_phone(value):
        phone_pattern = re.compile(r'\+375\((29|33|44|25)\)\d{7}')
        if not re.fullmatch(phone_pattern, str(value)):
            raise django.forms.ValidationError("Неверный формат номера телефона (правильный: +375(XX)XXXXXXX.")
    zooname = name = models.CharField(max_length=25, verbose_name="Zoo Name")
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, validators=[validate_phone])
    text = models.TextField()
    logo = models.ImageField(upload_to='images/', null = True)
"""
