from django.shortcuts import render
from django.views import View
from . models import Product
from django.db.models import Count

# Create your views here.
def home(request):
    return render(request, "app/home.html")

class KategorieView(View):
    def get(self, request, val):
        product = Product.objects.filter(kategoria = val)
        nazwa = Product.objects.filter(kategoria = val).values('nazwa').annotate(total=Count('nazwa'))
        return render(request, "app/category.html", locals())