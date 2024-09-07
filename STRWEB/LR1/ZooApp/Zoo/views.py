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
    latest_article = News.objects.latest('date')
    user_id = request.user.id
    is_staff = request.user.is_staff 
    is_super = request.user.is_superuser

    context = {
        'current_date_utc': current_date_utc.strftime('%d/%m/%Y %H:%M:%S'),
        'current_date_user_tz': current_date_user_tz.strftime('%d/%m/%Y %H:%M:%S'),
        'user_timezone': user_timezone.key,
        'latest_article': latest_article, 
        'user_id': user_id, 
        'is_staff': is_staff, 
        'is_super': is_super    
        }
    return render(request, 'home.html', context)

def news(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'news': news})

def animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals.html', {'animals':animals})

def about_company(request):
    user_id = request.user.id
    info = CompanyInfo.objects.first()
    return render(request, 'about.html', {'company_info': info, 'user_id': user_id})

def promocodes(request):
    promocodes = Promocode.objects.all()
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
    
class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        
        fields = ['username', 'first_name', 'last_name', 'age', 'phone', 'address', 'password1', 'password2']
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'age': 'Возраст',
            'phone': 'Телефон', 
            'address': 'Адрес',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
        }

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if request.user.is_authenticated:
                user.timezone = request.user.timezone
            else:
                user.timezone = get_localzone_name()
            #user.set_password(user.cleaned_data['password'])
            user.save()
            # Дополнительные действия после успешной регистрации
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

"""class UserRegistrationView(CreateView):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            logging.info("Registration form has no errors")
            user = form.save(commit=False)#commit=False
            #user.save()

            if request.user.is_authenticated:
                user.timezone = request.user.timezone
            else:
                user.timezone = get_localzone_name()
                        
            user.save()

            logging.info(f"{user.username} REGISTER (status: {user.status}) | user's Timezone: {user.timezone}")
            return redirect('login')
        else:
            logging.warning("Registration form is invalid")
            return render(request, 'registration.html', {'form': form})
"""

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


class TicketForm(forms.Form):
    date_of_visit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    promocode = forms.CharField(max_length=10, required=False)

class BuyTicket(View):
    def get(self, request,pk, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == "client":
            logging.info(f"{request.user.username} called OrderCreateView | user's Timezone: {request.user.timezone}")
            form = TicketForm()
            ticket = Ticket()
            return render(request, 'ticket_form.html', {'form': form, 'ticket': ticket})
    def post(self, request,pk, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == "client":
            form = TicketForm(request.POST)
            if form.is_valid():
                logging.info(f"OrderForm has no errors")
                Date_of_visit = form.cleaned_data['date_of_visit']
                code = form.cleaned_data['promocode']
                Price = 10.0
                def is_weekend():
                    return Date_of_visit.weekday() in [5, 6]
                
                print(type(Date_of_visit))

                promocode = Promocode.objects.filter(code=code).first()
                
                ticket =Ticket.objects.create(
                    user=request.user,
                    promocode=promocode,
                    price = Price,
                    date_of_visit = Date_of_visit
                )
                if promocode:
                        logging.info(f"Promocode {promocode.code} used by {request.user.username}")
                        ticket.use_discount(promocode)
                url = reverse('user_order', kwargs={"pk": ticket.user_id, "jk": ticket.id})
                return redirect(url)
            return render(request, 'ticket_form.html', {'form': form, 'ticket': ticket})
        elif request.user.is_authenticated and request.user.status == "staff":
            logging.error(f"{request.user.username} has status {request.user.status}")
            return HttpResponseNotFound("Только для клиентов")
        else:
            logging.error(f"User is not authenticated")
            return HttpResponse('Войдите в аккуант чтобы сделать заказ')

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