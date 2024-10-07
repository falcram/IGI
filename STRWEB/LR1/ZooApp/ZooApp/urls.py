"""
URL configuration for ZooApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, include
from Zoo import views , statistics
from django.conf.urls.static import static
from django.conf import settings

user_patterns = [
    re_path(r'orders', views.UserOrdersListView.as_view(), name='orders_list'),
    re_path(r'order/(?P<jk>\d+)', views.UserTicketView.as_view(), name='user_order'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('animals/', views.animals, name='animals'),
    path('about/', views.about_company, name='about'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),

    path('faqs/', views.faqs, name='faqs'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('reviews/', views.reviews, name='reviews'),
    path('review/create/', views.ReviewCreateView.as_view(), name='add_review'),
    path('review/<int:review_id>/edit/', views.ReviewEditView.as_view(), name='edit_review'),
    path('review/<int:review_id>/delete/', views.ReviewDeleteView.as_view(), name='delete_review'),
    path('promocodes/', views.promocodes, name="promocodes"),
    path('register/', views.register, name="register"),
    #path('register/', views.UserRegistrationView.as_view(), name="register"),
    #path('login/', views.my_login_view, name="login"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('contacts/', views.contacts, name='contacts'),
    path('contacts/new/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contacts/<int:pk>/edit/', views.ContactUpdateView.as_view(), name='contact_edit'),
    path('contacts/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),

    path('article/', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),

    
    re_path(r'user/(?P<pk>\d+)/', include(user_patterns)),
    path('order/<int:pk>/<int:jk>/', views.UserTicketView.as_view(), name='user_order'),
    path('order/<int:pk>/<int:jk>/cancel/', views.OrderCancelView.as_view(), name='order_cancel'),
    path('sales', statistics.sales, name='sales'),
    path('htmlstudy', views.htmlstudy_view, name='htmlstudy'),

    
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('add-to-cart/<int:ticket_date_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    # Успешная оплата
    path('success/', views.success_view, name='success'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('changeamount-in-cart/<int:item_id>/', views.changeamount_in_cart, name='changeamount_in_cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
