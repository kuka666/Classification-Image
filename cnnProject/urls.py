
from django.contrib import admin
from django.urls import path
from cnnApp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('predictImage', views.predictImage, name="predictImage")
    url(r'^media/(?P<path>.)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.)$', serve,{'document_root': settings.STATIC_ROOT}), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
