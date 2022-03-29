from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = request.GET.get('sort')
    print(sort_by)
    template = 'catalog.html'
    if sort_by == 'name':
        phone_objects = Phone.objects.order_by('name').all()
    elif sort_by == 'min_price':
        phone_objects = Phone.objects.order_by('price').all()
    elif sort_by == 'max_price':
        phone_objects = Phone.objects.order_by('price').all().reverse()

    phones = [{
        'slug': phone.slug,
        'name': phone.name,
        'price': phone.price,
        'image': phone.image
    } for phone in phone_objects]
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug)
    if len(phone_objects) > 0:
        phone_result = phone_objects[0]
        print(phone_result)
        phone = {
            'name': phone_result.name,
            'price': phone_result.price,
            'image': phone_result.image,
            'release_date': phone_result.release_date,
            'lte_exists': phone_result.lte_exists
        }
        context = {
            'phone': phone
        }
        return render(request, template, context)
    else:
        return HttpResponseNotFound(f'Такой модели нет')
