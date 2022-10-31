from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('king/', admin.site.urls),
    path('', include('kingnze.urls')),
    path('worldnews', include('worldnews.urls')),
    path('localnews', include('localnews.urls')),
    path('stportsnews', include('stportsnews.urls')),
    path('africanews', include('africanews.urls')),
    path('entertainment', include('entertainment.urls')),
    path('quote', include('quote.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
