
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clothing.views import loja_view
from accounts.views import register_view,login_view,logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', loja_view, name='cloth_list'),
    path('logout', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
