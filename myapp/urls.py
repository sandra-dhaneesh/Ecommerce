from django.urls import path,include
from. import views

urlpatterns = [
        path('',views.home,name='home'),
        path('log',views.log,name='log'),
        path('adminhome',views.adminhome,name='adminhome'),
        path('cushome',views.cushome,name='cushome'),
        path('signup',views.signup,name='signup'),
        path('add_customer',views.add_customer,name='add_customer'),
        path('cat',views.cat,name='cat'),
        path('add_category',views.add_category,name='add_category'),
        path('editcat/<int:pk>',views.editcat,name='editcat'),
        path('showcat',views.showcat,name='showcat'),
        path('deletecat/<int:pk>',views.deletecat,name='deletecat'),
        path('product',views.product,name='product'),
        path('add_prod',views.add_prod,name='add_prod'),
        path('editpro/<int:pk>',views.editpro,name='editpro'),
        path('showpro',views.showpro,name='showpro'),
        path('deletepro/<int:pk>',views.deletepro,name='deletepro'),
        path('usere',views.usere,name='usere'),
        path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
        path('categorized_products/<int:pk>/', views.categorized_products, name='categorized_products'),
        path('cart_details/<int:pk>',views.cart_details,name='cart_details'),
        path('removecart/<int:pk>',views.removecart,name='removecart'),
        path('cart',views.cart,name='cart'),
        path('logout',views.logout,name='logout'),

]