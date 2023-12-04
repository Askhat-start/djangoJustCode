from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from cart.forms import CartAddProductForm, CartNewProductForm


def cheap(request):
    cheap_items = Catalog.objects.filter(price__lte=5000)
    return render(request, 'main/base.html', {'items': cheap_items})


def exp(request):
    exp_items = Catalog.objects.filter(price__gte=6000)
    return render(request, 'main/exp.html', {'items': exp_items})


def base(request):
    items = Catalog.objects.all()
    cart_product_form = CartNewProductForm
    return render(request, 'main/base.html', {'items': items,
                                              'cart_product_form': cart_product_form})


def detail(request, item_id):
    try:
        item: object = Catalog.objects.get(id=item_id)
    except:
        return redirect('/')

    cart_product_form = CartAddProductForm
    return render(request, 'main/detail.html', {'item': item,
                                                'cart_product_form': cart_product_form})


def add(request):
    if request.method == 'POST':
        add_form = AddProduct(request.POST)
        if add_form.is_valid():
            # Form data is valid, save the data to the database
            name = add_form.cleaned_data['name']
            price = add_form.cleaned_data['price']
            description = add_form.cleaned_data['description']
            category = add_form.cleaned_data['category']

            print(name, price, description, category)
            # Now you can save the data to the database using a model
            # For example:
            # Product.objects.create(name=name, price=price, description=description, category=category)

    else:
        add_form = AddProduct()

    return render(request, 'main/add.html', {'add_form': add_form})



# CRUD
# Create
# Read
# Update
# Delete

"""
all()
get()
save()
delete()

count()
"""