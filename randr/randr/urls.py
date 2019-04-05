from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('pages.urls')),
    path('cart/', include('cart.urls')),
    path('books/', include('books.urls')),
    path('accessories/', include('accessories.urls')),
    path('events/', include('events.urls')),
    path('stores/', include('stores.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
