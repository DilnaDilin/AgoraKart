from django.db.models import Q
from django.shortcuts import render
from agorakartapp.models import Product

# Create your views here.
def searchProd(request):
    products=None
    query=None
    if request.method == 'GET' and 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__icontains=query)| Q(description__icontains=query))
    print(query)
    print(products)
    return render(request,'search.html',{'query':query, 'products':products})
