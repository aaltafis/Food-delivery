from django.shortcuts import render, get_object_or_404
from .models import Product, Category



def index(request):
	categories = Category.objects.all()
	context = {
		'categories': categories,
	}

	return render(request, "posts/index.html", context)


def category(request):	
	categories = Category.objects.all()
	context = {
		'categories': categories
	}

	return render(request, "posts/category.html", context)



def products(request, slug):
	categories = Category.objects.all()
	category = get_object_or_404(Category, slug=slug)
	product = Category.objects.get(slug=slug).product_set.all()
	context = {
		'categories': categories,
		'category': category,
		'product':product
	}

	return render(request, "posts/products.html", context)




def product_detail(request, category_slug, product_slug):
	categories = Category.objects.all()
	category = get_object_or_404(Category, slug=category_slug)
	product = get_object_or_404(Product, slug=product_slug)
	context = {
		'categories': categories,
		'product': product,
		'category': category
	}

	return render(request, "posts/product_detail.html", context) 







