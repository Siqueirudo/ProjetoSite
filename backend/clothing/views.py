from django.shortcuts import render
from clothing.models import cloth
from django.views.generic import ListView
# Create your views here.
class loja_view(ListView):
    model = cloth
    template_name = 'clothing.html'
    context_object_name = 'cloths'
    
    def get_queryset(self):
        cloths = super().get_queryset().order_by('category')
        search = self.request.GET.get('search')
        if search:
            cloths = cloth.objects.filter(
            Q(model__icontains=search) | 
            Q(value__icontains=search) | 
            Q(category__icontains=search))
        return cloths
    
