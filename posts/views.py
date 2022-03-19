from django.shortcuts import render
from .models import  Product, Category


def index(request):
	return render (request, "posts/index.html")

def our_menu(request):
	return render (request, "posts/our_menu.html")


def burgers(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	context = {
		'products': products,
		'categories': categories
	}
	return render(request, "posts/burgers.html")


