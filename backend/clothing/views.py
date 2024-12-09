from django.shortcuts import render
from django.http import HttpResponse
from clothing.models import cloth
# Create your views here.
def loja_view(request):
    cloths = cloth.objects.all()
    return render( request,'clothing.html',{'clothing': cloths })