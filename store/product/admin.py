from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (Product, Category, Brand, ProductLine,ProductAttribute,
                     AttributeValue, Attribute, Review, ShippingAddress, Order, CartItem)

from django.urls import reverse
from django.utils.safestring import mark_safe


class ProductLineInline(admin.TabularInline):
    model = ProductLine


class ProductAttributeValueInline(admin.TabularInline):
    model =AttributeValue.product_attribute.through


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline,ProductAttributeValueInline ]
    list_filter = ['category','brand']


class ProductLineAdmin(admin.ModelAdmin):

    # ordering = ProductLine.is_active
    list_filter = ['product']
    list_display = ['product', 'is_active']


class AttributeInline(admin.TabularInline):
    model = Attribute
    # list_display=['attribute']


class AttributeValueInline(admin.TabularInline):
    model =AttributeValue.category_attribute.through


class CategoryAdmin(admin.ModelAdmin):
    model=Category
    # inlines = [AttributeInline,AttributeValueInline ]
    inlines = [AttributeValueInline]
    list_display = ['id','name']


admin.site.register(Category, CategoryAdmin)
# admin.site.register(CategoryAttribute)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Attribute)
admin.site.register(AttributeValue)

admin.site.register(Review)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)


# class ListingAdmin(admin.ModelAdmin):
#     list_display=('id','title','price','is_published','list_date','coordinator')
#     list_display_links=('title',)
#     list_filter=('coordinator',)
#     list_editable=('is_published',)
#     search_fields=('title',)
#     list_per_page=2
# admin.site.register(Listing,ListingAdmin)
