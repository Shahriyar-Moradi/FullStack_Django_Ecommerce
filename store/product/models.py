from django.db import models

# Create your models here.
#
# from django.db.models.query import QuerySet
# from collections.abc import Collection, Iterable
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


class Attribute(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    # category_attribute_value = None
    attribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="attribute_value")

    def __str__(self):
        # return f"{self.attribute}"
        # return f"{self.attribute.name}"
        return f"{self.attribute.name} : {self.attribute_value}"


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/')
    parent_category = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True)
    attribute = models.ManyToManyField(AttributeValue, related_name="category_attribute", through="CategoryAttribute")
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class CategoryAttribute(models.Model):
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE,
                                        related_name="attribute_value_of_category")

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="category_attribute_value")

    def __str__(self):
        return self.category.name


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    photo_main = models.ImageField(upload_to='photos/%Y/%m/',null=True,blank=True)
    price = models.DecimalField(decimal_places=5, max_digits=10)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True)
    is_digital = models.BooleanField(max_length=200, default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    attribute = models.ManyToManyField(AttributeValue, related_name="product_attribute", through="ProductAttribute")
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.photo_main.url
    #     except:
    #         url = ''
    #     return url


class ProductAttribute(models.Model):
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE,
                                        related_name="attribute_value_of_product")

    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_attribute_value")

    def __str__(self):
        return self.product.name


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=5, max_digits=10)
    serial_number = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_line")
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()
    # photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # photo_one = models.ImageField(upload_to='photos/%Y/%m/%d/')

    # def clean(self, exclude=None):
    #     # super().clean_fields(exclude=exclude)
    #     qs = ProductLine.objects.filter(product=self.product)
    #     for obj in qs:
    #         if self.id == obj.id and self.attribute_value == obj.attribute_value:
    #             raise ValidationError('Duplicate value')
    #
    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super(ProductLine, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.product)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    rating = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=250, null=True, blank=True)
    tax_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # products=models.ManyToManyField(Product,through="CartItem")

    def __str__(self):
        return str(self.created_at)

    # @property
    # def get_total(self):
    #     total = self.product.price * self.quantity
    #     return total

    @property
    def get_cart_total(self):
        orderitems = self.order_items.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.order_items.all()
        total = sum([item.quantity for item in orderitems])
        return total


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='order_items')
    quantity = models.IntegerField(null=True, blank=True, default=0)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=250, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.order)