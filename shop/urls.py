from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('tracker/', views.tracker, name="tracker"),
    path('products/<int:myid>', views.productView, name="productView"),
    path('category/', views.category, name="category"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('men/', views.men, name="men"),
    path('women/', views.women, name="women"),
    path('womenview/<int:wid>', views.womenview, name="womenview"),
    path('kid/', views.kid, name="kid"),
    path('watch/', views.watch, name="watch"),
    path('shoe/', views.shoe, name="shoe"),
    path('other/', views.other, name="other"),
]
