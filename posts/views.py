from django.shortcuts import render, get_object_or_404
from .models import Product, Category



def index(request):
	categories = Category.objects.all()
	product = Product.objects.all()
	context = {
		'categories': categories,
		'product': product
		}
	return render(request, "posts/index.html", context)


def category(request):
	categories = Category.objects.all()
	context = {
		'categories': categories
	}

	return render(request, "posts/categories.html", context)



def products(request, slug):
	category = get_object_or_404(Category, slug=slug)
	product = Category.objects.get(slug=slug).product_set.all()
	context = {
		'category': category,
		'product':product
	}

	return render(request, "posts/products.html", context)




def product_detail(request, category_slug, product_slug):
	category = get_object_or_404(Category, slug=category_slug)
	product = get_object_or_404(Product, slug=product_slug)
	context = {
		'product': product,
		'category': category
	}

	return render(request, "posts/product_detail.html", context) 





















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


