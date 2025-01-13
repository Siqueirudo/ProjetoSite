
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clothing.views import loja_view,lojadetailview
from accounts.views import register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', loja_view.as_view(), name='cloth_list'),
    path('loj/<int:pk>/', lojadetailview.as_view(), name='cloth_detail'),
    #path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('loja/categoria/<str:category>/', loja_view.as_view(), name='cloth_category'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
