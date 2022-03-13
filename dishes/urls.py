from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name = "index"),
	path('collections/', views.categories_page_view, name = "categories"),
	path('collections/<slug:category_slug>/<slug:product_slug>/', views.product_detail_page_view, name = "product_detail"),
	path('collections/<slug:slug>/', views.category_product_page_view, name = "category_page"),
]