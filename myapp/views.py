import os
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from myapp.models import Customer,Category,Product,Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required(login_url='home')
def adminhome(requset):
    return render(requset,'adminhome.html')

@login_required(login_url='home')
def cushome(requset):
    prod=Category.objects.all()
    return render(requset,'cushome.html',{'prodct':prod})

def signup(requset):
    return render(requset,'signup.html')

@login_required(login_url='home')
def cat(requset):
    return render(requset,'cat.html')

@login_required(login_url='home')
def add_category(request):
    if request.method == "POST":
        cname=request.POST['cname']
        cat=Category(category_name=cname)
        cat.save()
        return redirect('showcat')
    return render(request,'add_category.html')

@login_required(login_url='signin')
def editcat(request,pk):
    if request.method == "POST":
        cas=Category.objects.get(id=pk)
        cas.category_name=request.POST['cname']
        cas.save()
        return redirect('showcat')
    cats=Category.objects.get(id=pk)
    return render(request,'editcat.html',{'category':cats})

@login_required(login_url='home')
def showcat(requset):
    cats = Category.objects.all()
    return render(requset,'showcat.html',{'cat':cats})

def deletecat(request,pk):
    det=Category.objects.get(id=pk)
    det.delete()   
    return redirect('showcat')

@login_required(login_url='home')
def product(requset):
    return render(requset,'product.html')

@login_required(login_url='home')
def add_prod(request):
    if request.method == "POST":
        pname=request.POST['pname']
        price=request.POST['price']
        description=request.POST['description']
        image = request.FILES.get('file')
        sel=request.POST['sel']
        category=Category.objects.get(id=sel)
        cato=Product(product_name=pname,price=price,description=description,image=image,category=category)
        cato.save()
        return redirect('showpro')
    cats=Category.objects.all()
    return render(request,'add_product.html',{'cate':cats})

def editpro(request,pk):
    if request.method == "POST":
        pro=Product.objects.get(id=pk)
        if len(request.FILES)!=0:
                if len(pro.image)>0:
                    os.remove(pro.image.path)
                pro.image=request.FILES.get('file')
        pro.product_name=request.POST['pname']
        pro.price=request.POST['price']
        pro.description=request.POST['description']
        sel=request.POST['sel']
        pro.category=Category.objects.get(id=sel)
        pro.save()
        return redirect('showpro')
    cats=Product.objects.get(id=pk)
    ca=Category.objects.all()
    return render(request,'editpro.html',{'category':cats,'cate':ca})

@login_required(login_url='home')
def showpro(request):
    pro = Product.objects.all()
    return render(request,'showpro.html',{'prod':pro})

def deletepro(request,pk):
    det=Product.objects.get(id=pk)
    det.delete()   
    return redirect('showpro')

def usere(request):
    cus = Customer.objects.all()
    return render(request,'showuser.html',{'custo':cus})

def deleteuser(request,pk):
    det=Customer.objects.get(user=pk)
    det.delete() 
    det=User.objects.get(id=pk)
    det.delete()     
    return redirect('usere')

def log(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['password']
        admin=auth.authenticate(username=username, password=password)
        
        if admin is not None:
            if admin.is_staff:
                login(request,admin)
                return redirect('adminhome')
            else:
                login(request,admin)
                auth.login(request,admin)
                messages.info(request, f'Welcome {username}')
                return redirect('cushome')
        else:
            messages.info(request, 'Invalid Username or Password. Please Try Again.')
            return redirect('/')

def add_customer(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        mob=request.POST['mob']
        username=request.POST['uname']
        address=request.POST['address']
        email=request.POST['mail']
        image = request.FILES.get('file')
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('home')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                det=Customer(mob=mob,address=address,user=user,image=image)
                det.save()
        else:
            messages.info(request, "Password doesn't match")
            return redirect('signup')   
        return redirect('signup')
    else:
        return render(request,'signup.html')


@login_required(login_url='home') 
def categorized_products(request, pk):
    categories = Category.objects.filter(id=pk)
    
    if categories.exists():
        category = categories.first()
        products = Product.objects.filter(category=category)
        return render(request, 'categories.html', {'categories': [category], 'products': products})
    else:
        
        return render(request, 'cushome.html')

@login_required(login_url='home') 
def cart(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cartitems':cart_items,'totalprice': total_price})

@login_required(login_url='home') 
def cart_details(request, pk):
    product = Product.objects.get(id=pk)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required(login_url='home') 
def removecart(request, pk):
    product = Product.objects.get(id=pk)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    
    if cart_item:
        cart_item.delete()
    
    return redirect('cart')

def logout(request):
    auth.logout(request)
    return redirect('home')
