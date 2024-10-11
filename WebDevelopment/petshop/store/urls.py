from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pet_list, name='pet_list'),  # 寵物列表
    path('products/', views.product_list, name='product_list'),  # 產品列表
    path('dogs/', views.dog_breeds, name='dog_breeds'),
    path('cats/', views.cat_breeds, name='cat_breeds'),
]
