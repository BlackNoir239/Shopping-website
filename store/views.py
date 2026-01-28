# store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products, 'categories': categories})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'store/category.html', {'category': category, 'products': products, 'categories': categories})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', {'product': product})

def checkout(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        # Here is where you would normally process the payment (e.g., save order to DB)
        # For this demo, we just assume payment is successful.
        return redirect('success')

    return render(request, 'store/checkout.html', {'product': product})

def payment_success(request):
    return render(request, 'store/success.html')