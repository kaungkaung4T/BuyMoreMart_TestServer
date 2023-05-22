from django.shortcuts import render, redirect
from app_controller.Application.models import User
from app_controller.Order.models import Cart, Product, Order
from django.http import JsonResponse

class Order_class:
    def check_out(self, request):
        cart_delivery_fee = request.POST['cart_delivery_fee']
        cart_total = request.POST['cart_total']
        cart_total_items = request.POST['cart_total_items']

        cart_grand_total_price = int(cart_total) + int(cart_delivery_fee)


        # create order of all products from cart
        user_relative_cart = Cart.objects.filter(user=request.user)
        cart_json = {}

        for each_cart in user_relative_cart:
            cart_json[each_cart.product.title] = each_cart.amount


        instant = Order.objects.create(user=request.user, each_product=cart_json,
                            grand_total_price=cart_grand_total_price, delivery_fee=cart_delivery_fee,
                            total_items=cart_total_items)

        # first method for adding order
        for each_cart2 in user_relative_cart:
            instant.product.add(each_cart2.product)
        
        # second method for adding order
        # instant.product.set(each_cart.product for each_cart in user_relative_cart)

        
        return redirect('order_success')
