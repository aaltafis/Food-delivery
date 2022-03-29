from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30, verbose_name="Название")
	slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, verbose_name="URL")
	image = models.ImageField(upload_to="category_image/", null=True, blank=True, verbose_name="Изображение")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('products', args=[self.slug])


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return super().save(*args, **kwargs)



	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"


class Product(models.Model):
	title = models.CharField(max_length=50, verbose_name="Название")
	price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ImageField(upload_to="product_images/", null=True, blank=True)
	slug = models.SlugField(null=True,  blank=True, unique=True, db_index=True, verbose_name="URL")

	def __str__(self):
		return f"{self.title} - {self.category}"

	def get_absolute_url(self):
		return reverse('product_detail', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super().save(*args, **kwargs)


	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары" 
