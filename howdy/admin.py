from django.contrib import admin
from .models import Category,Product,Order
from .models import Cart, User

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('id','name','price','Description','Image','category')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user','sub_total','qty','product','order_id')


class oderAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','phone','grand_total','address')

admin.site.register(User)
admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order)

