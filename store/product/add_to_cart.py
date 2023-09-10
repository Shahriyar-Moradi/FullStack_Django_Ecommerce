# # def add_to_cart(request, product_id):
# #     product = get_object_or_404(Product, pk=product_id)
# #     cart_item, created = OderItem.objects.get_or_create(
# #         user=request.user,
# #         product=product
# #     )
# #
# #     if not created:
# #         # The product is already in the cart, so you can increase the quantity if needed
# #         cart_item.quantity += 1
# #         cart_item.save()
# #
# #     return redirect('cart')  # Redirect to the cart page or any other desired page
#
#
# # def add_to_cart(request, product_id):
# #     product = get_object_or_404(Product, pk=product_id)
# #     order, created = Order.objects.get_or_create(user=request.user)
# #     cart_item, _ = CartItem.objects.get_or_create(
# #         order=order,
# #         product=product
# #     )
# #     cart_item.quantity += 1
# #     cart_item.save()
# #
# #     return redirect('cart')  # Redirect to the cart page or any other desired page
# #
#
#
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     order, created = Order.objects.get_or_create(user=request.user)
#     cart_item, item_created = CartItem.objects.get_or_create(product=product, order=order)
#     if not item_created:
#         cart_item.quantity += 1
#         cart_item.save()
#     cart_items = CartItem.objects.filter(order=order)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})
