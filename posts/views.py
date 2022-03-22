from django.shortcuts import render, get_object_or_404
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

def salads(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	context = {
		'products': products,
		'categories': categories
	}
	return render(request, "posts/salads.html")


def snacks(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	context = {
		'products': products,
		'categories': categories
	}
	return render(request, "posts/snacks.html")

def potatoes(request):
	return render(request, "posts/potatoes.html")

def soups(request):
	return render(request, "posts/soups.html")

def sauces(request):
	return render(request, "posts/sauces.html")

def beverages(request):
	return render(request, "posts/beverages.html")


