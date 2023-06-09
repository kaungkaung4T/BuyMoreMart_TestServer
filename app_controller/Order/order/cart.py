from django.shortcuts import render, redirect
from app_controller.Application.models import User, Product_type
from app_controller.Order.models import Cart, Product
from app_controller.PaymentAndDelivery.models import Delivery_fee
from django.http import JsonResponse, HttpResponse
from app_controller.Website_Interface.models import Info, Header_ImageGroup

class Cart_class:
    def home(self, request):
        # Info
        if Info.objects.filter(id=1).exists():
            info = Info.objects.get(id=1)
        else:
            info = None

        # Header Image
        if Header_ImageGroup.objects.filter(id=1).exists():
            header_image = Header_ImageGroup.objects.get(id=1)
        else:
            header_image = None

        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

        if request.user.is_authenticated == False:
            return redirect('login')

        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        delivery_fees = Delivery_fee.objects.all()

        if request.user.is_authenticated:
            items = Cart.objects.filter(user=request.user)
            total_item = Cart().total_item(request.user)
            total_type = len(list(items))
            all_total_price = Cart().all_total_price(request.user)

            grand_total_price = all_total_price + delivery_fees[0].delivery_fee
            
        else:
            items = None
            total_item = 0
            total_type = 0
            all_total_price = 0
            grand_total_price = 0
            

        context = {
            'info': info,
            'header_image': header_image,

            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "items": items,
            "total_item": total_item,
            "total_type": total_type,
            "all_total_price": all_total_price,
            "delivery_fees": delivery_fees,
            "grand_total_price": grand_total_price,
            "cart_noti": cart_len
        }
        return render(request, 'order/cart.html',
                    context)


    def cancel_cart(self, request, cart_item_id):
        if request.method == 'POST':
            cart = Cart.objects.get(id=cart_item_id)
            cart.delete()

            return redirect('cart')

        return redirect('cart')


    def add_cart(self, request):
        if request.method == 'POST':
            if request.user.is_authenticated == False:
                context = {
                "response": "no_user"
                }
                return JsonResponse(context)

            product_id = request.POST['product_id']
            product = Product.objects.get(id=product_id)
            user = User.objects.get(id=request.user.id)

            if Cart.objects.filter(user=user, product=product).exists():
                context = {
                "response": "duplicate"
                }
                return JsonResponse(context)
            else:
                if product.discount:
                    Cart.objects.create(user=user, product=product, total_price=product.discount)
                else:
                    Cart.objects.create(user=user, product=product, total_price=product.price)
                context = {
                "response": "added"
                }
                return JsonResponse(context)
            
            return JsonResponse(context)

        context = {
            "response": ""
            }
        return JsonResponse(context)
    

    def one_product_add_cart(self, request):
        if request.method == 'POST':
            if request.user.is_authenticated == False:
                context = {
                "response": "no_user"
                }
                return JsonResponse(context)

            product_id = request.POST['one_product_id']
            product_new_amount = request.POST['amount']


            product = Product.objects.get(id=product_id)
            user = User.objects.get(id=request.user.id)

            if product.discount:
                new_total_price = int(product_new_amount) * product.discount
            else:
                new_total_price = int(product_new_amount) * product.price


            if product_new_amount:
                if Cart.objects.filter(user=user, product=product).exists():
                    existing_cart = Cart.objects.get(user=user, product=product)

                    if existing_cart.amount == int(product_new_amount):
                        context = {
                        "response": "duplicate"
                        }
                        return JsonResponse(context)
                    else:
                        existing_cart.amount = product_new_amount
                        existing_cart.total_price = new_total_price

                        existing_cart.save()
                        context = {
                        "response": "updated"
                        }
                        return JsonResponse(context)


            if Cart.objects.filter(user=user, product=product).exists():
                context = {
                "response": "duplicate"
                }
                return JsonResponse(context)
            else:
                if product.discount:
                    Cart.objects.create(user=user, product=product, amount=product_new_amount, total_price=new_total_price)
                else:
                    Cart.objects.create(user=user, product=product, amount=product_new_amount, total_price=new_total_price)
                context = {
                "response": "added"
                }
                return JsonResponse(context)
            
            return JsonResponse(context)

        context = {
            "response": ""
            }
        return JsonResponse(context)
