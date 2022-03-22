"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('our_menu', views.our_menu, name = "our_menu"),
    path('burgers', views.burgers, name = "burgers"),
    path('salads', views.salads, name = "salads"),
    path('snacks', views.snacks, name="snacks"),
    path('potatoes', views.potatoes, name="potatoes"),
    path('soups', views.soups, name="soups"),
    path('sauces', views.sauces, name="sauces"),
    path('beverages', views.beverages, name="beverages"),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


