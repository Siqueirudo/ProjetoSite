from django.shortcuts import render
from clothing.models import cloth
# Create your views here.
def loja_view(request):
    cloths = cloth.objects.all().order_by('category')
    search = request.GET.get('search')

    if search:
        cloths = cloths.filter(category__icontains=search).order_by('category')
    return render( request,'clothing.html',{'cloths': cloths })