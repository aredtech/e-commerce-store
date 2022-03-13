from django.shortcuts import render
from store.models import Product
from django.db.models import Q

# Create your views here.
def index(request):

    queryset = Product.objects.filter(Q(id__gte=1) | Q(id__lte=4)).order_by("-title")
    return render(request, "front_page/index.html", {
        "products" : list(queryset)
    })