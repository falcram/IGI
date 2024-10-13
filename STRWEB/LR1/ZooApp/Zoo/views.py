from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth.views import LoginView
from django.views.generic import *
from django.views import View
from django.contrib.auth.models import auth
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils import timezone
from datetime import datetime
from tzlocal import get_localzone
from django.forms import inlineformset_factory
import pytz
import requests
import logging
from django.contrib.auth import authenticate, login


logging.basicConfig(level=logging.INFO, filename='logging.log', filemode='a', format='%(asctime)s %(levelname)s %(message)s')

def home(request):
    user_timezone = get_localzone()

    current_date_utc = timezone.now()
    current_date_user_tz = current_date_utc.astimezone(user_timezone)
    latest_article = Article.objects.latest('date')
    user_id = request.user.id
    is_staff = request.user.is_staff 
    is_super = request.user.is_superuser
    partners = Partner.objects.all()  # Получаем всех партнеров из базы данных
    context = {
        'current_date_utc': current_date_utc.strftime('%d/%m/%Y %H:%M:%S'),
        'current_date_user_tz': current_date_user_tz.strftime('%d/%m/%Y %H:%M:%S'),
        'user_timezone': user_timezone.key,
        'latest_article': latest_article, 
        'user_id': user_id, 
        'is_staff': is_staff, 
        'is_super': is_super,
        'partners': partners    
        }
    return render(request, 'home.html', context)

def animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals.html', {'animals':animals})

def about_company(request):
    user_id = request.user.id
    info = CompanyInfo.objects.first()
    return render(request, 'about.html', {'company_info': info, 'user_id': user_id})

def promocodes(request):
    promocodes = PromoCode.objects.all()
    return render(request, 'promocodes.html', {'promocodes': promocodes})

def faqs(request):
    faqs = FAQ.objects.all()
    return render(request, 'faqs.html', {'faqs': faqs})

def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies': vacancies})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(label='Оценка', min_value=1, max_value=5)
    class Meta:
        model = Review
        fields = ['title', 'rating','text']
        labels = {
            'title': 'Тема',
            'rating': 'Оценка',
            'text': 'Текст',
        }

class ReviewCreateView(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated and request.user.status == 'client':
            
            logging.info(f"{request.user.username} called ReviewCreateView (status: {request.user.status}) | user's Timezone: {request.user.timezone}")

            form = ReviewForm()
            is_staff = request.user.is_staff 

            return render(request, 'review_create_form.html', {'form': form, 'is_staff': is_staff})
        return redirect('login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == 'client':
            form = ReviewForm(request.POST)
            if form.is_valid():
                logging.info(f"ReviewForm has no errors)")

                title = form.cleaned_data['title']
                rating = form.cleaned_data['rating']
                text = form.cleaned_data['text']

                review = Review.objects.create(title=title, rating=rating, text=text, user=request.user)
                logging.info(f"Review '{review.title}' was created by {request.user.username} ")
                return redirect('reviews')
        logging.warning("User is not authenticated")
        return redirect('login')

class ReviewEditView(View):
    def get(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        if request.user.is_authenticated and review.user == request.user:
            form = ReviewForm(instance=review)
            return render(request, 'review_edit.html', {'form': form, 'review': review})
        return redirect('login')

    def post(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        if request.user.is_authenticated and review.user == request.user:
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews')
        return render(request, 'review_edit.html', {'form': form, 'review': review})

class ReviewDeleteView(View):
    def get(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        if request.user.is_authenticated and review.user == request.user:
            review.delete()
        return redirect('reviews')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'age', 'phone', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.status = 'client'  # Устанавливаем статус "client" по умолчанию
        if commit:
            user.save()
        return user

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически авторизуем пользователя после регистрации
            return redirect('home')  # Переход на главную страницу после успешной регистрации
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def my_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Пользователь аутентифицирован, устанавливаем сеанс
            login(request, user)
            return redirect('home')  # Перенаправляем на страницу профиля
        else:
            # Неверные учетные данные, обработайте ошибку
            pass
    # Отображение формы входа
    return render(request, 'login.html')

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    #auth.login(request)
    #def get_success_url(self):  
    #    logging.info("User LOGIN")
    #    return reverse_lazy('home')
            
class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            #logging.info(f"{request.user.username} LOGOUT (status: {request.user.status}) | user's Timezone: {request.user.timezone}")
            auth.logout(request)
            return render(request, 'logout.html')
        return redirect('home')

def privacy_policy(request):
    return render(request, 'privacy.html')

def contacts(request):
    contacts = Contact.objects.all()
    is_super = request.user.is_superuser
    return render(request, 'contacts.html', {'contacts': contacts, 'is_super': is_super})

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['description', 'user', 'photo']

class ContactCreateView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contacts_form.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            logging.info(f"Contact '{contact.user.username}' was created")
            return redirect('contacts')  
        return render(request, 'contacts_form.html', {'form': form})

class ContactUpdateView(View):

    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(instance=contact)
        return render(request, 'contacts_form.html', {'form': form, 'contact': contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            logging.info(f"Contact '{contact.user.username}' was updated")
            return redirect('contacts') 
        return render(request, 'contacts_form.html', {'form': form, 'contact': contact})

class ContactDeleteView(View):
    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        contact.delete()
        return redirect('contacts')  

class UserTicketView(View):
    def get(self, request, pk, jk, *args, **kwargs):
        if request.user.is_authenticated and request.user.id==int(pk) and Ticket.objects.filter(user_id=int(pk), id=int(jk)).exists():
            logging.info(f"{request.user.username} called SpecificOrderView | user's Timezone: {request.user.timezone}")

            order = Ticket.objects.filter(user_id=pk, id=jk).first()

            return render(request, 'order_detail.html', {'order': order})
        return HttpResponseNotFound("Страница не найдена")
    
class UserOrdersListView(View):
    def get(self, request, pk, *args, **kwargs):

        if request.user.is_authenticated and request.user.id==int(pk):
            logging.info(f"{request.user.username} called UserOrderView | user's Timezone: {request.user.timezone}")
            order = Ticket.objects.filter(user_id=pk)
            return render(request, "orders_list.html", {'orders': order})

        logging.error(f"Call failed UserOrderView")
        return HttpResponseNotFound("Страница не найдена")

class OrderCancelView(View):
    def post(self, request, pk, jk, *args, **kwargs):
        if request.user.is_authenticated and request.user.id == int(pk):
            ticket = get_object_or_404(Ticket, user_id=pk, id=jk)
            if not ticket.is_canceled:
                ticket.is_canceled = True
                ticket.save()
                logging.info(f"Order '{ticket.id}' was canceled by {request.user.username}")
            return redirect('user_order', pk=pk, jk=jk)
        return HttpResponseNotFound("Страница не найдена")
    
def htmlstudy_view(request):
    return render(request, 'htmlstudy.html')

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})


def ticket_list(request):
    # Извлекаем все доступные даты для билетов
    ticket_dates = TicketDate.objects.filter(available_quantity__gt=0).order_by('date')
    
    return render(request, 'ticket_list.html', {
        'ticket_dates': ticket_dates
    })

def add_to_cart(request, ticket_date_id):
    ticket_date = get_object_or_404(TicketDate, id=ticket_date_id)

    if request.method == 'POST':
        print("POST data: ",request.POST, sep="\n")
        quantity = int(request.POST.get('quantity', 1))
        print(quantity)
        # Проверяем доступное количество билетов
        if ticket_date.available_quantity < quantity:
            return render(request, 'error.html', {'error': 'Недостаточно билетов на выбранную дату'})

        # Если всё ок, создаем или обновляем элемент корзины
        cart_item, created = CartItem.objects.get_or_create(user=request.user, ticket_date=ticket_date)
        cart_item.quantity += quantity
        cart_item.save()

        # Уменьшаем количество доступных билетов
        ticket_date.available_quantity -= quantity
        ticket_date.save()

    return redirect('cart')

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    print(cart_items)
    total_cost = sum(item.ticket_date.ticket.price * item.quantity for item in cart_items)
    
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_cost': total_cost
    })

# Страница оплаты
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        promo_code = request.POST.get('promo_code', None)
        
        # Проверяем промокод
        if promo_code:
            try:
                promo = PromoCode.objects.get(code=promo_code)
            except PromoCode.DoesNotExist:
                return render(request, 'error.html', {'error': 'Неверный промокод'})
        else:
            promo = None

        # Создаем заказ
        order = Order.objects.create(user=request.user, promo_code=promo)
        order.items.set(cart_items)
        order.is_paid = True  # Имитация оплаты
        order.total_price = order.get_total_cost()
        order.save()
        print(order.total_price)
        
        message = f"{order.total_price} руб. Оплата прошла успешно!"
        cart_items.delete()
        return render(request, 'success.html', {
        'message': message
        })

    total_cost = sum(item.ticket_date.ticket.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_cost': total_cost})

def success_view(request, price):
    message = f"{price} руб. Оплата прошла успешно!"
    return render(request, 'success.html', {
        'message': message
    })

def clear_cart(request):
    # Удаляем все элементы корзины текущего пользователя
    cart_item = CartItem.objects.filter(user=request.user)
    for item in cart_item:
        ticket_date = item.ticket_date
        ticket_date.available_quantity += item.quantity
        ticket_date.save()
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart')  # П


def changeamount_in_cart(request, item_id):
    print("changeamount_in_cart start")
    cart_item = get_object_or_404(CartItem, id=item_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', cart_item.quantity))
        if quantity != cart_item.quantity:
            ticket_date = cart_item.ticket_date
            ticket_date.available_quantity += cart_item.quantity - quantity
            ticket_date.save()
            cart_item.quantity=quantity
            cart_item.save()

    return redirect('cart')

def order_list(request):
    orders = Order.objects.all()  # Получаем все заказы
    return render(request, 'order_list.html', {'orders': orders})