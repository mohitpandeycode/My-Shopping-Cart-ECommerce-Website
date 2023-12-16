from django.urls import path
from . import views


# creating shop pipeline
urlpatterns = [
    path('',views.index ,name='ShopHome'),
    path('about/',views.about ,name='About Us'),
    path('contact/',views.contact,name='Contact US'),
    path('tracker/',views.tracker ,name='Tracker'),
    path('search/',views.search ,name='Search'),
    path('products/<int:myid>',views.productView ,name='ProductView'),
    path('checkout/',views.checkout ,name='Checkout'),
    path('handlerequest/',views.handlerequest ,name='HandleRequest')

   ]