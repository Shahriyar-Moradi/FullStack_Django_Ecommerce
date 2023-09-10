"""Ecom_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from . import views
# from django.conf.urls import
urlpatterns = [
    path('', views.index, name='index'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('products/fetch_products/<category_id>',views.fetch_products,name="fetch_products"),
    path('product_filter/',views.product_filter,name="product_filter"),
    path('categories/<category_id>/', views.get_products_by_category, name='products_by_category'),
    # path('categories/<category_id>/brand/<int:brand_id>/', views.filter_data, name='products_by_category_brand'),
    #



    # path('search',views.search,name='search'),

    # path('products/brands/<brand_id>/', views.get_products_by_brand, name='products_by_brand'),
    # path('category/<id>', views.get_products_by_category_paged, name='products_by_category_paged'),
    # path('category/', views.get_products_by_category, name='products_by_category'),
    # path(r'^categories/(?P<category_id>[\w-]+)/$', views.get_products_by_category, name='products_by_category'),
    # re_path(r'^categories/(?P<category_id>\w+)/', views.get_products_by_category, name='products_by_category'),
    # re_path(r"categories/(?P<category_id>\w+)", views.get_products_by_category, name='products_by_category'),

    path('product_line/<int:product_line_id>/', views.get_product_line, name='single_product_line'),
    path('product_lines/<int:product_id>/', views.get_product_line_by_product, name='product_line_product'),
    # path('product/<int:product_id>/', views.get_product, name='get_product'),
]
