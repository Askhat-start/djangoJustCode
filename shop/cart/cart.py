from decimal import Decimal
from django.conf import settings
from main.models import Catalog
import json

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # Save an empty cart in the session
            cart = {}

        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Catalog.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            if str(product.id) in cart:
                cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * Decimal(item['quantity']) if item['quantity'] > 0 else Decimal('0')
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            # If the product was not initially in the cart
            self.cart[product_id] = {'quantity': 0, 'price': Decimal(product.price)}

        self.cart[product_id]['quantity'] = int(quantity)

        print('QUANTITY INBORD', quantity)
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = json.loads(json.dumps(self.cart, default=str))
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        total_price = 0
        for item in self.cart.values():
            print('Quantity', item['quantity'], 'Price', item['price'])
            total_price += int(item['quantity']) * int(item['price'])
        return total_price

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.save()
