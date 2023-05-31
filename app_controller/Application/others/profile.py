from django.shortcuts import render, redirect
from app_controller.Application.models import User, Product_type
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from app_controller.Application.verification import send_otp, send_email
from app_controller.Order.models import Cart

class Profile:
    def home(self, request):
        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

        if request.method == "POST":
            phone = request.POST["phone"]
            name = request.POST["name"]
            email = request.POST["email"]
            address = request.POST["address"]
            city = request.POST["city"]
            country = request.POST["country"]

            if request.user.is_authenticated:
                user = User.objects.get(id=request.user.id)
                
                if phone:
                    user.phone_number = phone
                elif name:
                    user.username = name
                elif email:
                    user.email = email
                elif address:
                    user.address = address
                elif city:
                    user.city = city
                elif country:
                    user.country = country

                user.save()
                messages.success(request, "Successfully Update!")
            
            else:
                messages.info(request, "Please register an account!")

            return redirect("profile")
        
        if request.user.is_authenticated == False:
            return redirect("login")

        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0
        
        context = {
            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "cart_noti": cart_len
        }

        return render(request, 'others/profile.html',
                    context)


    def security(self, request):
        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

        if request.method == "POST":
            password = request.POST["password"]
            password2 = request.POST["password2"]

            if password == password2:
                if request.user.is_authenticated:
                    user = User.objects.get(id=request.user.id)

                    otp = send_otp(user.phone_number)
                    send_email(user.username, user.email, otp)

                    user.otp = otp
                    user.save()

                    return redirect(f"/profile_verification/{password}")
                
                messages.info(request, "Please register an account!")
                return redirect("security")
            
            else:
                messages.info(request, "Passwords do not match!")
                return redirect("security")

        if request.user.is_authenticated == False:
            return redirect("login")

        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0
        
        context = {
            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "cart_noti": cart_len
        }

        return render(request, 'others/profile_password.html',
                    context)
        

    def profile_verification(self, request, new_password):
        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

        if request.method == "POST":
            otp = request.POST["otp"]
            
            if request.user.is_authenticated:
                user = User.objects.get(id=request.user.id)

                if user.otp == otp:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)

                    messages.success(request, "Successfully Update!")
                    return redirect("security")

                else:
                    if request.user.is_authenticated:
                        cart = Cart.objects.filter(user=request.user)
                        cart_len = len(list(cart))
                    else:
                        cart_len = 0
                        
                    context = {
                        'header_food': header_food,
                        'header_accessories': header_accessories,
                        'header_beauty': header_beauty,

                        "new_password": new_password,
                        "cart_noti": cart_len
                    }
                    messages.info(request, "Entered a wrong code. Please check the number and try again!")
                    return render(request, "others/profile_verification.html",
                                    context)
            
            
            messages.info(request, "Please register an account!")
            return redirect("registration")
        
        if request.user.is_authenticated:
            if request.user.is_authenticated:
                cart = Cart.objects.filter(user=request.user)
                cart_len = len(list(cart))
            else:
                cart_len = 0

            context = {
                'header_food': header_food,
                'header_accessories': header_accessories,
                'header_beauty': header_beauty,

                "new_password": new_password,
                "cart_noti": cart_len
            }

            return render(request, "others/profile_verification.html",
                                    context)
        
        else:
            return redirect("login")

