
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clothing.views import loja_view,lojadetailview
from accounts.views import register_view, login_view, logout_view
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', loja_view.as_view(), name='cloth_list'),
    path('loj/<int:pk>/', lojadetailview.as_view(), name='cloth_detail'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('login/',login_view, name='login'),
    path('loja/categoria/<str:category>/', loja_view.as_view(), name='cloth_category'),
    path('whoweare', TemplateView.as_view(template_name='whoweare.html'), name='whoweare'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


