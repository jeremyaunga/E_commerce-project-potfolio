from django.db import models
from django.contrib.auth.models import User
#customer model
class CustomerProfile(models.Model):
    extended_user = models.OneToOneField(User, on_delete=models.CASCADE)  # Renamed to extended_user
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.extended_user.username  # Updated the reference to extended_user.username
class Catergory(models.Model):
    name = models.CharField(max_length=100)   

    class Meta:
        verbose_name_plural = 'catergories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    catergory = models.ForeignKey(Catergory,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)    
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.name
    def get_price(self):
        return self.price
#order model
class Order(models.Model):
    customer_profile = models.OneToOneField(CustomerProfile,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    payment_id = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return f"order{self.id} by {self.customer_profile.extended_user.username}"
#orderitem
class Orderitem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    def get_total_price(self):
        return self.price*self.quantity
    def __str__(self):
        return f"{self.quantity}x{self.product.name}"
#cart model get customer name

#cart item list
class Cartitem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def get_total_price(self):
        return self.product.price*self.quantity
    def __str__(self):
        return f"{self.quantity}x{self.product.name}"
#payment
class Payment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f"payment{self.id} for order {self.order.id}"

