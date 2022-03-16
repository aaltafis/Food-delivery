from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request):
	"""
	Главная страница
	""" 

	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, "dishes/index.html", context)


def categories_page_view(request):
	""" 
	Страница со всеми категориями
	"""
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, "dishes/categories.html", context)


def category_product_page_view(request, slug):
	""" 
	Страница с продуктами определённой категории
	"""
	category = get_object_or_404(Category, slug=slug)
	products = Category.objects.get(slug=slug).product_set.all()

	context = {
		'category': category,
		'products':products,
	}

	return render(request, "dishes/products.html", context)

def product_detail_page_view(request, category_slug, product_slug):
	""" 
	Страница детального просмотра продукта
	"""
	category = get_object_or_404(Category, slug=category_slug)
	product = get_object_or_404(Product, slug=product_slug)

	context = {
		'product': product,
		'category': category,
	}

	return render(request, "dishes/product_detail.html", context)