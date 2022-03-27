from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	# admin
    path('admin/', admin.site.urls),

    # user-management
    path('accounts/', include('django.contrib.auth.urls')),

    # local
    path('', include('dishes.urls')),
    path('users/', include('users.urls')),
    path('', include(('cart.urls', 'cart_detail'), namespace='cart')),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)