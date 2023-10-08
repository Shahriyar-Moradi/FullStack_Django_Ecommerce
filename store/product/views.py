from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from .models import Category, Product, ProductLine, Order, CartItem, Brand
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest
from .utils import cookieCart, cartData, guestOrder
from django.http import JsonResponse
import json
import datetime
from django.core import serializers
from django.urls import resolve
from django.db import connection
from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import TerminalFormatter
# from pygments.lexers import
from sqlparse import format
from django.http import HttpResponse
from django.db.models import Prefetch
from django.db import reset_queries


def index(request):
    # listings=Listing.objects.order_by('-price')
    # categories = Category.objects.all()
    products = Product.objects.all()
    # paginator = Paginator(listings, 3)
    # page = request.GET.get('page')
    # paged_list = paginator.get_page(page)
    context = {
        'products': products,
        # 'categories': categories,

        # 'categories': categories,

    }
    return render(request, 'products/index.html', context)


def get_products_by_category(request: HttpRequest, category_id):
    reset_queries()
    # category_idd = None
    # if 'category_id' in request.resolver_match.kwargs:
    #     category_idd = request.resolver_match.kwargs['category_id']
    # print("category_idddd", category_idd)

    brands = Brand.objects.all()
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category).select_related('category')

    # all_attributes = category.category_attribute_value.all()
    # print("all_attributes", all_attributes)
    q = list(connection.queries)
    print("queries counts", len(q))
    for qs in q:
        sqlformatted = format(str(qs['sql']), reindent=True)
        print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))

    context = {
        'products': products,
        # 'products_paged_list': products_paged_list,
        'brands': brands,
        # 'category': category,
        # 'attributes': all_attributes,
        'category_id': category_id,
    }
    return render(request, 'products/products_of_category.html', context)


def get_single_product(request: HttpRequest, product_id):
    # product = Product.objects.filter(pk=product_id)
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/single_product.html', context)


def get_product_line_by_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_lines = ProductLine.objects.select_related('product').filter(product=product)
    # single_product_line=get_object_or_404(ProductLine,product_id=product_id)
    # single_product_line=ProductLine.objects.filter(product=product).first()

    print("plll", product_lines)
    context = {
        # 'single_product_line': single_product_line,
        'product_lines': product_lines,
    }
    return render(request, 'Pages/product_line.html', context)


def get_product_line(request, product_line_id):
    single_product_line = ProductLine.objects.get(id=product_line_id)
    # single_product_line = product.product_line.first()
    # single_product_line = ProductLine.objects.filter(product=product).first()
    phot = Product.photo_main
    print("photo", phot)
    print("single", single_product_line)
    print('single')
    context = {
        'single_product_line': single_product_line,
    }
    return render(request, 'Pages/single_product_line.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'products/cart.html', context)




def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'products/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=customer)

    orderItem, created = CartItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    elif action == 'delete':
        orderItem.quantity = orderItem.quantity = 0
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def product_filter(request):

    brands = Brand.objects.all()
    categories=Category.objects.all()
    selected_brand_ids = request.GET.getlist('brands[]')
    print('selected', selected_brand_ids)
    products = Product.objects.filter(brand__id__in=selected_brand_ids)

    return render(request, 'products/products_of_category_ajax.html', {'brands': brands,
                                                                       'categories': categories,
                                                                       'products':products})


def fetch_products(request,category_id):

    reset_queries()
    selected_brand_ids = request.GET.getlist('brands[]')
    print('seleceted_brands',selected_brand_ids)
    category = Category.objects.get(id=category_id)
    allProducts = Product.objects.filter(category=category).all()
    if len(selected_brand_ids) > 0:
        allProducts = allProducts.filter(category=category,brand__id__in=selected_brand_ids).distinct()
    all = render_to_string('products/products_of_category_ajax.html', {'data': allProducts})
    return JsonResponse({'data': all})

# q = list(connection.queries)
#         print("queries counts",len(q))
#         for qs in q :
#             sqlformatted=format(str(qs['sql']),reindent=True)
#             print(highlight(sqlformatted,SqlLexer(),TerminalFormatter()))
        # q = list(connection.queries)
        # sqltime = 0.0 # Variable to store execution time
        # for query in connection.queries:
        #     sqltime += float(query["time"])  # Add the time that the query took to the total
        #     print("Page render: "+ str(sqltime)+ "sec for "+ str(len(connection.queries))+ " queries")
        # for qs in q :
        #     sqlformatted=format(str(qs['sql']),reindent=True)
        #     print(highlight(sqlformatted,SqlLexer(),TerminalFormatter()))
        # print("select_related queries counts",len(q))
