from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('success/', views.payment_success, name='success'),
]