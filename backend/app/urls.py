
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from clothing.views import loja_view



urlpatterns = [
    path('admin/', admin.site.urls),
     path('loja/', loja_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
