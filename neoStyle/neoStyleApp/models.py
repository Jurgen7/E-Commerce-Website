from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=60)
    contact_email = models.EmailField(null=True, blank=True)
    contact_message = models.TextField(max_length=1000,null=True, blank=True)

    def __str__(self):
        return f"{self.contact_name}"

class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.color_name}"

class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.size_name}"

class Filter(models.Model):
    filter_id = models.AutoField(primary_key=True)
    filter_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.filter_name}"
    
class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.brand_name}"
    
class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.gender_name}"

# Product

class Product(models.Model):
    product_name = models.CharField(max_length=60, null=True, blank=True)
    product_category = models.CharField(max_length=60, null=True, blank=True)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    product_id = models.AutoField(primary_key=True)
    product_image = models.ImageField(upload_to="product/", null=True, blank=True)
    product_image2 = models.ImageField(upload_to="product/", null=True, blank=True)
    product_image3 = models.ImageField(upload_to="product/", null=True, blank=True)
    product_image4 = models.ImageField(upload_to="product/", null=True, blank=True)
    product_description = models.TextField(max_length=1000, null=True, blank=True)
    product_color = models.ManyToManyField(Color)
    product_size = models.ManyToManyField(Size)
    
    product_filter = models.ForeignKey(Filter, on_delete=models.CASCADE, null=True, blank=True)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    product_gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.product_name}-{self.product_id}"
      

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='customer')
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		if self.name:
			name = self.name
		else:
			name = self.device
		return str(name)
	
# Order

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = True
		return shipping
        
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	
	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total
	

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.product_price * self.quantity
        return total

# Shipping

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

# Newsletter

class NewsletterUser(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    email = models.ManyToManyField(NewsletterUser)
    status = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body




