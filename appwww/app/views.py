from django.shortcuts import render
from django.views import View
from . models import Product
from django.db.models import Count
from . forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "app/home.html")

def onas(request):
    return render(request, "app/onas.html")

def kontakt(request):
    return render(request, "app/kontakt.html")

class KategorieView(View):
    def get(self, request, val):
        product = Product.objects.filter(kategoria = val)
        nazwa = Product.objects.filter(kategoria = val).values('nazwa').annotate(total=Count('nazwa'))
        return render(request, "app/category.html", locals())

class nazwaKategorii(View):
    def get(self, request, val):
        product = Product.objects.get(nazwa = val)
        nazwa = Product.objects.filter(kategoria = product[0].kategoria).values('nazwa')
        return render(request, "app/kategoria.html", locals())

class ProductDesc(View):
    def get(self, request, pk):
        product = Product.objects.get(pk = pk)
        return render(request, "app/productdesc.html", locals())

class RegistrationView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'app/registerform.html', locals())
    def post(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rejestracja przebiegła pomyślnie! Możesz się zalogować.")
        else:
            messages.warning(request, "Złe dane.")
        return render(request, "app/registerform.html", locals())


