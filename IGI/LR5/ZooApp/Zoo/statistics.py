import base64
from datetime import datetime
import io
from urllib import parse

from django.http import HttpResponseNotFound
import numpy as np
from statistics import median, mode, mean
import matplotlib
from django.db.models import Sum, Count, Avg

from .models import *
from matplotlib import pyplot as plt
from django.shortcuts import render

def clients(request): 
    if request.user.is_authenticated and request.user.is_superuser:   
        clients = User.objects.filter(status='client').order_by('first_name')
        ages = []
        for client in clients:
            ages.append(client.age)

        average_age = round(mean(ages), 2)
        median_age = round(median(ages), 2)

        return render(request, 'clients_stat.html', {'clients': clients,
                                                'average_age': average_age,
                                                'median_age': median_age,
                                                })
    return HttpResponseNotFound("Page not found")




def sales(request):
    if request.user.is_authenticated and request.user.is_superuser: 
        orders = Ticket.objects.filter(is_canceled=False)
        prices = []
        general_sales = 0.0
        for order in orders:
            prices.append(order.price)
            general_sales += order.price
    
        average_sales = round(mean(prices), 2)
        median_sales = round(median(prices), 2)
        mode_sales = round(mode(prices), 2)

        url, yearly_sales_data = linear_sales_trend()
        image_urls = year_sales_volume()

        return render(request, 'sale_stat.html', {'general_sales': general_sales,
                                                'average_sales': average_sales,
                                                'median_sales': median_sales,
                                                'mode_sales': mode_sales,
                                                'image': url, 
                                                'yearly_sales_data': yearly_sales_data,
                                                'image_urls': image_urls,
                                                })
    return HttpResponseNotFound("Page not found")


def yearly_sales_report(year):
    print(type(year))
    print(year)
    orders = Ticket.objects.filter(date_of_visit__year =year, is_canceled=False)
    total_sales_for_year = orders.aggregate(total_sales=Sum('price'))['total_sales'] or 0
    return total_sales_for_year


def yearly_sales_trend():
    current_year = datetime.now().year
    last_three_years = range(current_year - 2, current_year + 1)
    yearly_sales_ = []

    for year in last_three_years:
        sales = yearly_sales_report(year)
        yearly_sales_.append(round(sales, 2))

    return list(last_three_years), yearly_sales_


def linear_sales_trend():

    matplotlib.use('Agg')

    years, sales = yearly_sales_trend()

    plt.figure(figsize=(14, 6))

    plt.plot(years, sales, color='yellowgreen', marker='o', linestyle='-')
    plt.xlabel('Год')
    plt.ylabel('Общее преимущество, руб')
    plt.title('Продажи за год')
    plt.xticks(years)
    plt.grid(True)


    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = parse.quote(string)

    yearly_sales_data = list(zip(years, sales))

    return url, yearly_sales_data


def year_sales_volume():
    matplotlib.use('Agg')

    years, sales = yearly_sales_trend()

    image_urls = []

    colors = ['yellowgreen', 'yellowgreen', 'yellowgreen']

    plt.figure(figsize=(10, 10))

    plt.bar(years, sales, color=colors)
    plt.xlabel('Год')
    plt.ylabel('Продажи, руб')
    plt.xticks(years)
    plt.title(f'Продажи за год - {years}')

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = parse.quote(string)

    image_urls.append(url)

    return image_urls


def class_diagramm(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'diagram.html')
    return HttpResponseNotFound("Page not found")
