from django.shortcuts import render
from store.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):
    products = Product.objects.all().filter(is_available=True)
    paginator = Paginator(products, 4)     # show three products in first page of store
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
    }
    return render(request, 'home.html', context)