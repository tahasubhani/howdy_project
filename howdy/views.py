from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from .models import Product,Category,Cart,Order
from django.contrib.auth.decorators import login_required
from .forms.userform import createform
from .forms.orderform import Orderform
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from sms import send_sms
from sms import Message
#_______________________________HOME____________________________________________________#
def home(request):
    # product = Product.objects.all()
    # category = Category.objects.all()
    # return HttpResponse(product)
    return render(request,'home.html')
#_-_____________________________MENU____________________________________________________#

def menu(request):
    category_products =  category = Category.objects.all()
    Categorys_name = ''
    return render(request,'menu.html',{'category_products': category_products,'categories':category,'Categorys_name':Categorys_name})
#______________________________SHOW_CART________________________________________________#
@login_required(login_url='create_account')
def show_cart(request):
    if request.method == "POST":
        id = request.POST.get('product_id')

        qty = int(request.POST.get('qty'))  

        user = request.user 

        product = Product.objects.get(pk=id)

        cart_item, create = Cart.objects.get_or_create(product=product, user = user,order_id =0)

        if  create:
            cart_item.qty = qty
            sub_total = qty * product.price
            cart_item.sub_total = sub_total
            cart_item.user = request.user
            cart_item.save()
        else:
            cart_item.qty += qty
            sub_total = cart_item.qty * product.price
            cart_item.sub_total = sub_total 
            cart_item.save()

    cart_items = Cart.objects.filter(user=request.user,order_id =0)
    sub_total = 0

    for cart in cart_items:
        sub_total += cart.sub_total

    grand_total = float(sub_total)*0.13
    grand_total+= float(sub_total)

    return render(request, 'show_cart.html',{'cart_items':cart_items, 'sub_total':sub_total,'grand_total':grand_total})
#______________________________CHECKOUT_________________________________________________#

def checkout(request):
    cart_items =Cart.objects.filter(user =request.user,order_id =0)
    sub_total = 0

    for cart in cart_items:
        sub_total += cart.sub_total

    grand_total = float(sub_total)*0.13
    grand_total+= float(sub_total)
    
    if  request.method == 'POST':
        form = Orderform(request.POST)
        
        if form.is_valid:

            form_order = form.save(commit=False)

            
            if request.user is not None:
                form_order.user = request.user

            if request.POST.get('order_amount'):
                form_order.oders_amount = request.POST.get('order_amount')
    
            if request.POST.get('paymentMethod'):
                    form_order.payment_mode = request.POST.get('paymentMethod')


            form_order.save()

            cart_items = Cart.objects.filter( user = request.user,order_id =0)
            for cart_item in cart_items:

                cart_item.order_id = form_order.id
                messages.success(request,("You Order is placed Check your email"))
                cart_item.save()

                subject = 'New order is Placed'
                msg_plain = loader.render_to_string('order_email.txt', {'cart_items': cart_items, 'grand_total':grand_total})
                msg_html = loader.render_to_string('order_email.html', {'cart_items': cart_items, 'grand_total':grand_total})
                form_email = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email']]
                send_mail(subject,msg_plain,form_email,recipient_list, html_message=msg_html)
            else:
                return redirect('order')
    else:
        form =Orderform()
        return render(request,'checkout.html',{'form':form,'cart_items':cart_items, 'sub_total':sub_total,'grand_total':grand_total})  
#_____________________________CHECK_TO_POROCEED_________________________________________#

def check_to_proceed(request):
    if request.user.is_authenticated:

        return redirect('checkout')
    if request.method == "POST":
        # return HttpResponse(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password )
        # return HttpResponse(user)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))

            print('logged in')
            return render(request,'home.html')
        else:
            messages.error(request, ("You Have Been Logged In!"))
            print('error')
            return redirect('check_to_proceed')  
    else:
        return render(request,'check_to_proceed.html')
#______________________________CREATE_ACCOUNT___________________________________________#
            
def create_account(request):
    if request.method == 'POST':
        form = createform(request.POST)
        if form.is_valid:
            # return HttpResponse(form.errors)
            form.save()
            return redirect('check_to_proceed')
        else:
            return redirect('create_account')
    else:
        form = createform()
        # return HttpResponse(form)
        return render( request,'create_account.html',{'form': form})
#_________________________________LOGOUT________________________________________________#

def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged out!"))
    return redirect('check_to_proceed')
#_________________________________DELETE________________________________________________#

def delete_user(request,id): 

    Cart_delet =Cart.objects.get(id=id)
    Cart_delet.delete()

    cart_items = Cart.objects.filter( user = request.user,order_id= 0)

    # agr koi ak chiz exsits karti ha to exsits use ho ga 
    
    if cart_items.exists():
        return redirect('show_cart')
    else:
        return redirect('menu')
#________________________________category_items_________________________________________#

def category_items(request,id):
    category_object = Category.objects.get(id=id)
    Categorys_name = category_object.name  
    # products =Product.objects.filter(category = category_object)
    # return HttpResponse(products)
    categories = Category.objects.all()
    category_products = Category.objects.filter(id=id)
    return render(request,'menu.html',{'category_products':category_products,'Categorys_name':Categorys_name,'categories':categories})
#___________________________________Email_______________________________________________#
   
def email(request):
    cart_items = Cart.objects.filter(user=request.user,order_id=0)
    sub_total = 0


    for cart in cart_items:
        sub_total += cart.sub_total

    grand_total = float(sub_total)*0.13
    grand_total+= float(sub_total)

    message_body = loader.get_template('order_email.html')
    return HttpResponse(message_body.render({'cart_items': cart_items, 'grand_total':grand_total }))
#___________________________________Email_______________________________________________#

def order_confirm(request):
    cart_items = Cart.objects.all()
    order = Order.objects.all()
    # return HttpResponse(cat)
    sub_total = 0
    for cart in cart_items:
        sub_total += cart.sub_total
    grand_total = float(sub_total)*0.13
    grand_total+= float(sub_total)
    return render(request,'confirm_oder.html',{'cart_items':cart_items,'grand_total':grand_total,'order':order  })
