from django.shortcuts import render, redirect
from django.contrib import messages
from.models import *

from django.http import JsonResponse
import json
import datetime

from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

from django.conf import settings
from django.template.loader import get_template

from django.core.mail import send_mail, EmailMultiAlternatives
from . models import NewsletterUser, Newsletter
from .forms import NewsletterUserSignupForm

from .utils import cookieCart, cartData, guestOrder

from django.core.paginator import Paginator

from django.http import HttpResponse


# Create your views here.

def home_view(request):
    products = Product.objects.all().order_by("-product_id")

    data = cartData(request)
    cartItems = data['cartItems'] 

    context = {
        'products': products,
        'cartItems': cartItems,
    }

    return render(request, 'home.html', context)

def about_view(request):
    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems':cartItems,}
    return render(request, 'about.html', context)

def contact_view(request):
    data = cartData(request)
    cartItems = data['cartItems']   

    if request.method == "POST":
        firstName = request.POST['firstName']
        email = request.POST['email']
        message = request.POST['sms']
        Contact(
                contact_name = firstName,
                contact_email = email,
                contact_message = message
            ).save()
        
        # messages.success(request, 'Message sent successfuly!')
    
    context = {'cartItems':cartItems,}
    
    return render(request, 'contact.html', context)

def products_view(request):
    products = Product.objects.all()

    filter_id = request.GET.get('filters')
    brand_id = request.GET.get('brands')
    gender_id = request.GET.get('genders')

    if filter_id:
        products = products.filter(product_filter_id=filter_id)
    elif brand_id:
        products = products.filter(product_brand_id=brand_id)
    elif gender_id:
        products = products.filter(product_gender_id=gender_id)

    # Filter by price
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price and max_price:
        products = products.filter(product_price__range=(min_price, max_price))

    # Pagination
    paginator = Paginator(products, 9) # 9 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)

    data = cartData(request)
    cartItems = data['cartItems']

    context = {
        'products':products,
        'cartItems':cartItems
    }

    return render(request, 'products.html', context)

def product_view(request, id):
    product = Product.objects.get(product_id=id)

    data = cartData(request)
    cartItems = data['cartItems']

    context = {"product":product, 'cartItems':cartItems,}
    return render(request, 'product.html', context)


def cart_view(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems,}
    return render(request, 'cart.html', context)


def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # In that case we render informations that we store in cookies (cookieData function/utils.py)
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items'] 
        
    context = {'items':items, 'order':order, 'cartItems':cartItems,}
    return render(request, 'checkout.html', context)

#Order

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(product_id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
				
    else:
        # Anonymous User -- created a function(guestOrder/utils.py) to send the informations in our database
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
                )

    return JsonResponse('Payment submitted..', safe=False)

# Login/Register

def register_view(request):

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            #saving the registered user
            user = register_form.save()
            Customer.objects.create(
                user = user,
                name = user.username,
                email = user.email
            )
            username= register_form.cleaned_data.get('username')             
            return redirect('login')
    else:
        register_form = RegisterForm() 

    context = {'register_form':register_form}
    return render(request, 'register.html',context)

def login_view(request):

    if request.method == "POST":
        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    else:
        login_form = LoginForm()
        
    context = {'login_form':login_form}
    return render(request, 'login.html', context)

def logout_view(request):
    auth.logout(request)
    return redirect('home')

# Newsletter

def newsletter_signup(request):
    form = NewsletterUserSignupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your have already subscribed', 'alert alert-light alert-dismissible')
        else:
            instance.save()
            messages.success(request, 'Your Email has been submitted successfully', 'alert alert-light alert-dismissible')
            subject = 'Thank you for Joining our Community'
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]

            with open(settings.BASE_DIR / 'templates/newsletter/sign_up_email.txt') as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject,
                body=signup_message,
                from_email=from_email,
                to=to_email
            )
            html_template = get_template('newsletter/sign_up_email.html').render()
            message.attach_alternative(html_template, 'text/html')
            message.send()
        return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
    }
    return HttpResponse(context)
