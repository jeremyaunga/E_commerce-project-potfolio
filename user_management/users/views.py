from django.shortcuts import render,redirect,get_object_or_404
from users.forms import SignUpForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from users.models import CustomerProfile,Product,Cartitem
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from users.models import Catergory

# Create your views here.
@login_required
def user_profile(request):
    user = request.user   
    return render(request,"user_profile.html",{"user":user})
def home(request):
    return render(request,'base.html') 
# handles login
def login_user(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"invalid credentials")
            return redirect('login')
        else:
            login(request,user)
            messages.success(request,"successfully logged in !!!")
            return redirect('homepage')
    else:
        return render(request,'login.html')
def logout_user(request):
    logout(request)
    messages.success(request,("you have been logged out !!!!!!!"))
    return redirect('homepage')    
def authenticated_user(request):
    user= request.user
    current_time = current_hour = timezone.now().hour        
    return render(request,"homepage.html",{"user":user,"current_time":current_time})


#handles signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
             # Authenticate the user after registration
            user = authenticate(request, username=username, password=password)            
            if user is not None:
                # Log the user in if authentication is successful
                login(request, user)
                messages.success(request, 'Successfully registered and logged in')
                return redirect('homepage')
            else:
                # If authentication fails, show an error message
                messages.error(request, "Invalid credentials")
                return redirect('signup')  # Redirect back to the signup page in case of failure
    else:
        form = SignUpForm()
    # Ensure form is returned in case of GET request or invalid POST
    return render(request, 'signup.html', {'form': form})
#to show list of users
def users_list(request):
    profiles = request.user #gets users
    if profiles.is_authenticated:
        user = CustomerProfile.objects.all()
    return render(request,"users_list.html",{"profiles":profiles,"user":user})
#for homepage
def homepage(request):
    all_products = Product.objects.all()
    return render(request,"homepage.html",{"all_products":all_products})    
#register products
@login_required
def register_product(request):
    if request.method == 'POST':
        # Get form data
        catergory_name = request.POST['catergory']
        name = request.POST['name']
        description = request.POST.get('description', '')
        price = request.POST['price']
        stock = request.POST['stock']

        # Handle the checkbox value
        available = True if request.POST.get('available') == 'on' else False

        image = request.FILES.get('image', None)

        # Check if the category already exists
        catergory, created = Catergory.objects.get_or_create(name=catergory_name)

        # Create the product, setting the user as the authenticated user
        product = Product.objects.create(
            catergory=catergory,
            user=request.user,  # Automatically set the current user
            name=name,
            description=description,
            price=price,
            stock=stock,
            available=available,
            image=image,
        )
        return redirect('homepage')  # Redirect to a success page

    # GET request: render the empty form
    return render(request, 'register_product.html')
#handle items in cart
@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    cart_item,created = Cartitem.objects.get_or_create(user = request.user,product=product)
    if not created:
        cart_item.quantity +=1 
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()
    return redirect('homepage')
@login_required
def view_cart(request):
    if request.user.is_authenticated:
        cart_items = Cartitem.objects.filter(user=request.user)
         # Calculate the total price of the items in the cart
        total_price = sum(item.product.price * item.quantity for item in cart_items)                
        total_items = sum(item.quantity for item in cart_items)
    else:
        cart_items = []
        total_price = 0
        total_items = 0
    return render(request,"view_cart.html",{"cart_items":cart_items,"total_price":total_price,"total_items":total_items})


    
        