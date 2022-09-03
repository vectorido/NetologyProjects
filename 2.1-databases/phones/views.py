from django.shortcuts import render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', None)
    if sort == 'name':
        phone = list(Phone.objects.all().order_by('name'))
    elif sort == 'min_price':
        phone = list(Phone.objects.all().order_by('price'))
    elif sort == 'max_price':
        phone = list(Phone.objects.all().order_by('price').reverse())
    else:
        phone = list(Phone.objects.all())

    template = 'catalog.html'
    context = {
        'phones': phone,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
