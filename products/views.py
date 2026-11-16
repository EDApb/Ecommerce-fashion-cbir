from django.shortcuts import render
# Create your views here.
from .models import Product
from django.shortcuts import render, get_object_or_404
from .clip_search import search


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def product_search(request):
    query = request.GET.get('q', '')
    products = []
    if query:
        ids = search(query)
        products = [Product.objects.get(pk=i) for i in ids]
    return render(request, 'products/product_list.html',
                  {'products': products, 'query': query})