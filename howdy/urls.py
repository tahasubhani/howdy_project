from django.urls import path
from . import views
#_____________________________________URLS________________________________________________#
urlpatterns = [
    path("",views.home ,name='home'),
    path("menu/",views.menu ,name='menu'),
    path("show_cart/",views.show_cart , name='show_cart'),
    path("create_account/",views.create_account ,name='create_account'),
    path("check_to_proceed/",views.check_to_proceed ,name='check_to_proceed'),
    path("checkout/",views.checkout ,name='checkout'),
    path("category/<int:id>",views.category_items , name ='category_items'),
    path("logout_user/",views.logout_user ,name='logout_user'),
    path("delete_user/<int:id>",views.delete_user ,name='delete_user'),
    path('email/',views.email),
    path('order_confirm/',views.order_confirm ,name='order')
]
