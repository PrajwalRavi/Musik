from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin,auth

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
