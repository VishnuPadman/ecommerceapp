from django.shortcuts import render
from ecapp.models import Product
from django.db.models import Q

def searchresult(request):
    products=None
    querry=None
    if 'q'in request.GET:
        querry=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=querry) | Q(description__contains=querry))
        return render(request, 'search.html',{'querry':querry, 'products':products})