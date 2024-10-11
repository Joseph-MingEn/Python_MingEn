from django.shortcuts import render
from .models import Pet, Product

# Create your views here.

def home(request):
    pets = Pet.objects.all()
    products = Product.objects.all()
    return render(request, 'store/home.html', {'pets': pets, 'products': products})

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'store/pet_list.html', {'pets': pets})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def dog_breeds(request):
    dogs = Pet.objects.filter(species=Pet.DOG)
    return render(request, 'store/dog_breeds.html', {'dogs': dogs})

def cat_breeds(request):
    cats = Pet.objects.filter(species=Pet.CAT)
    return render(request, 'store/cat_breeds.html', {'cats': cats})