from django.http import HttpRequest ,HttpResponse

from .models import Category, Product, ProductLine,Order
from django.views import View

from django.urls import reverse
from django.shortcuts import get_object_or_404

from django.db.models import Prefetch
from .utils import cookieCart, cartData, guestOrder


def extra(request):
    categories = Category.objects.all()
    parents_categories = Category.objects.filter()
    products = Product.objects.all()

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user)
        cartItems = order.get_cart_items

    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'categories': categories,
            'parents_categories': parents_categories,
            'products': products,
            'cartItems': cartItems,
            }
