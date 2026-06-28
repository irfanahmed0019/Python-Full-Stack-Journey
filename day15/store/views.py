from django.shortcuts import render, get_object_or_404,redirect
from .models import Product,CartItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required

# -------------------------
# Store Pages
# -------------------------

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product.html", {"product": product})

# -------------------------
# Cart Actions
# -------------------------
@login_required(login_url="login")
def cart(request):
    cart_items=CartItem.objects.filter(user=request.user)
    total=sum(item.total_price for item in cart_items)
    context={
        "cart_items":cart_items,
        "total":total,
    }
    return render(request, "cart.html",context)


def review(request):
    return render(request, "review.html")


def shipping(request):
    return render(request, "shipping.html")


def order(request):
    return render(request, "order.html")


def payment(request):
    return render(request, "payment.html")


def confirmed(request):
    return render(request, "confirmed.html")


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")

def increase_quantity(request,id):
    cart_item=get_object_or_404(CartItem,id=id,user=request.user)

    cart_item.quantity+=1
    cart_item.save()
    return redirect("cart")

def decrease_quantity(request,id):
    cart_item=get_object_or_404(CartItem,id=id,user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity-=1
        cart_item.save()
    
    else:
        cart_item.delete()
    return redirect("cart")
 
def delete_cart_item(request,id):
    cart_item=get_object_or_404(CartItem,id=id,user=request.user)
    cart_item.delete()
    return redirect("cart")

# -------------------------
# Authentication
# -------------------------

def continue_login(request):
    email = request.session.get("email")

    context = {
        "email": email,
    }

    if request.method == "POST":
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            context["error"] = "Incorrect password."

    return render(request, "continue_login.html", context)

def login(request):
    if request.method == "POST":
        email=request.POST.get("email")
        if User.objects.filter(email=email).exists():
            request.session["email"]=email
            return redirect("continue_login")
        else:
            request.session["email"]=email
            return redirect("new_user")
    return render(request,"login.html")

def signup(request):
    email=request.session.get("email")
    context={
        "email":email,
    }
    if request.method=="POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        password_check=request.POST.get("password_check")
        if password==password_check:
            User.objects.create_user(
                username=email,
                first_name=name,
                email=email,
                password=password
            )
            user= authenticate(
                request,
                username=email,
                password=password
            )
            auth_login(request,user)
            return redirect("home")
        else:
            context["error"]="Password do not match"
    return render(request,"signup.html",context)

def reset_password(request):
    email=request.session.get("email")
    context={"email":email,}
    return render(request,"reset_password.html",context)

def forgot_password(request):
    return render(request,"forgot_password.html")

def new_user(request):
    email=request.session.get("email")
    context={"email":email}
    return render(request,"new_user.html",context)

@login_required(login_url="/auth/")
def user_dashboard(request):
    context={
        "user":request.user
    }
    return render(request,"user_dashboard.html",context)

def logout_user(request):
    logout(request)
    return redirect("home")