from .models import Filter, Brand, Gender, Product
from .forms import NewsletterUserSignupForm
from .views import newsletter_signup

def my_context_processor(request):
    
    products = Product.objects.all()

    filters = Filter.objects.all()
    brands = Brand.objects.all()
    genders = Gender.objects.all()

    filter_id = request.GET.get('filters')
    brand_id = request.GET.get('brands')
    gender_id = request.GET.get('genders')

    if filter_id:
        products = products.filter(product_filter_id=filter_id)
    elif brand_id:
        products = products.filter(product_brand_id=brand_id)
    elif gender_id:
        products = products.filter(product_gender_id=gender_id)

    # Newsletter
    newsletter_signup(request)  # call the newsletter_signup view
    form = NewsletterUserSignupForm()  # create a new form instance
        

    return {'filters': filters, 'brands': brands, 'genders': genders, 'form': form,}