from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home_view, name='home'),
    path ('about/', views.about_view, name='about'),
    path ('contact/', views.contact_view, name='contact'),
    path ('products/', views.products_view, name='products'),
    path ('product/<id>', views.product_view, name='product'),
    
    path ('cart/', views.cart_view, name='cart'),
    path ('checkout/', views.checkout_view, name='checkout'),
    
    path ('update_item/', views.updateItem, name='updateItem'),
    path('process_order/', views.processOrder, name="process_order"),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup'),
]

