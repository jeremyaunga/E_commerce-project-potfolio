from django.contrib import admin
from users.models import CustomerProfile,Product,Cartitem,Payment,Catergory,Order,Orderitem



# Register your models.
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('extended_user', 'phone_number', 'date_joined')  # Fields to display
    search_fields = ('extended_user__username', 'phone_number')  # Fields to search by
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(Product)
admin.site.register(Cartitem)
admin.site.register(Orderitem)
admin.site.register(Order)
admin.site.register(Catergory)
admin.site.register(Payment)

