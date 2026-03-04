from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request):
    product=Product.objects.all().filter(is_available=True)
    context={
        'product': product,
        'product_count': product.count(),
    }
    return render(request, 'store/store.html', context)