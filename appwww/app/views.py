from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from . models import Product, Client, Basket, Payment, Order
from django.db.models import Count
from . forms import UserRegisterForm, ClientProfileForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import razorpay

# Create your views here.
@login_required
def home(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Basket.objects.filter(user=request.user))
    return render(request, "app/home.html", locals())

def onas(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Basket.objects.filter(user=request.user))
    return render(request, "app/onas.html", locals())

def kontakt(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Basket.objects.filter(user=request.user))
    return render(request, "app/kontakt.html", locals())

@method_decorator(login_required, name='dispatch')
class KategorieView(View):
    
    def get(self, request, val):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Basket.objects.filter(user=request.user))
        product = Product.objects.filter(kategoria = val)
        nazwa = Product.objects.filter(kategoria = val).values('nazwa').annotate(total=Count('nazwa'))
        return render(request, "app/category.html", locals())

@method_decorator(login_required, name='dispatch')
class nazwaKategorii(View):
    def get(self, request, val):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Basket.objects.filter(user=request.user))
        product = Product.objects.get(nazwa = val)
        nazwa = Product.objects.filter(kategoria = product[0].kategoria).values('nazwa')
        return render(request, "app/kategoria.html", locals())

@method_decorator(login_required, name='dispatch')
class ProductDesc(View):
    def get(self, request, pk):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Basket.objects.filter(user=request.user))
        product = Product.objects.get(pk = pk)
        return render(request, "app/productdesc.html", locals())

class RegistrationView(View):
    def get(self, request):
        form = UserRegisterForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Basket.objects.filter(user=request.user))
        return render(request, 'app/registerform.html', locals())
    def post(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rejestracja przebiegła pomyślnie! Możesz się zalogować.")
        else:
            messages.warning(request, "Złe dane.")
        return render(request, "app/registerform.html", locals())

@method_decorator(login_required, name='dispatch')
class UserView(View):
    def get(self, request):
        form = ClientProfileForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Basket.objects.filter(user=request.user))
        if request.user == 'admin':
            user = 'admin'
        return render(request, 'app/user.html', locals())

    def post(self,request):
        form = ClientProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            imie = form.cleaned_data['imie']
            miasto = form.cleaned_data['miasto']
            ulica = form.cleaned_data['ulica']
            numer_domu_mieszkania = form.cleaned_data['numer_domu_mieszkania']
            telefon = form.cleaned_data['telefon']
            wojewodztwo = form.cleaned_data['wojewodztwo']
            kodPocztowy = form.cleaned_data['kodPocztowy']

            saveit = Client(user = user, imie = imie, miasto = miasto,ulica=ulica, numer_domu_mieszkania=numer_domu_mieszkania, telefon=telefon, wojewodztwo = wojewodztwo, kodPocztowy = kodPocztowy)
            saveit.save()
            messages.success(request, "Dane adresowe zapisane pomyślnie!")
        else:
            messages.warning(request, "Wprowadzone dane adresowe są błędne!")
        return render(request, 'app/user.html', locals())

@login_required
def adres(request): #tylko pobranie danych z bazy i wyswietlenie na uipage
    adres = Client.objects.filter(user=request.user) #fetchuj ClientProfile tylko gdy user = login/username
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Basket.objects.filter(user=request.user))
    return render(request, 'app/adres.html', locals())

@method_decorator(login_required, name='dispatch')
class updateAdres(View):
    def get(self, request, pk):
        add = Client.objects.get(pk=pk) # chcemy tylko row nie array
        form = ClientProfileForm(instance=add)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Basket.objects.filter(user=request.user))
        return render(request, 'app/updateAdres.html', locals())
    def post(self, request, pk):
        form = ClientProfileForm(request.POST)
        if form.is_valid():
            add = Client.objects.get(pk=pk) #get data i trzymaj w add + wyswietl w formularzach
            add.imie = form.cleaned_data['imie'] ## wez imie i updateuj
            add.miasto = form.cleaned_data['miasto']
            add.ulica = form.cleaned_data['ulica']
            add.numer_domu_mieszkania = form.cleaned_data['numer_domu_mieszkania']
            add.kodPocztowy = form.cleaned_data['telefon']
            add.wojewodztwo = form.cleaned_data['wojewodztwo']
            add.telefon = form.cleaned_data['telefon']
            add.save()#zapisz
            messages.success(request, "Dane kontaktowe zaaktualizowano pomyślnie!")
        else:
            messages.warning(request, "Złe dane kontaktowe!")
        return redirect("adres")

@login_required
def add_to_basket(request):
    user = request.user #potrzebny user
    product_id = request.GET.get('prod_id') #get product it ktory chcemy dodac do koszyka
    product = Product.objects.get(id = product_id) # produkt dla modulu basket nadpisz z 
    Basket(user=user,product=product).save() #dodaj rekord do basket table
    return redirect("/basket")

@login_required
def buy_now(request):
    user=request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    Basket(user=user,product=product).save()
    return redirect("/checkout")

@login_required
def show_basket(request):
    user = request.user
    basket = Basket.objects.filter(user=user)
    il = 0
    for i in basket:
        cost = i.amount * i.product.cena
        il = il + cost
    total = il + 10
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Basket.objects.filter(user=request.user))
    return render(request, 'app/addtobasket.html', locals())

def plus_basket(request):
    if request.method=='GET':

        prod_id = request.GET['prod_id']
        c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user)) #q jest 
        c.amount += 1
        c.save()
        user = request.user
        basket = Basket.objects.filter(user=user)
        ile=0
        for i in basket:
            value = i.amount * i.product.cena
            ile = ile + value
        totalcost = ile + 10
        data ={
            'amount':c.amount,
            'ile':ile,
            'totalcost':totalcost

        }
        return JsonResponse(data)

def minus_basket(request):
    if request.method=='GET':

        prod_id = request.GET['prod_id']
        c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.amount -= 1
        c.save()
        user = request.user
        basket = Basket.objects.filter(user=user)
        ile=0
        for i in basket:
            value = i.amount * i.product.cena
            ile = ile + value
        totalcost = ile + 10
        data ={
            'amount':c.amount,
            'ile':ile,
            'totalcost':totalcost

        }
        return JsonResponse(data)

def remove_basket(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        basket = Basket.objects.filter(user=user)
        ile=0
        for i in basket:
            value = i.amount * i.product.cena
            ile = ile + value
        totalcost = ile + 10
        data ={
            'ile':ile,
            'totalcost':totalcost

        }
        return JsonResponse(data)


    # if request.method =='GET':
    #     prod_id = request.GET['prod_id']
    #     c = Basket.objects.filter(Q(product=prod_id) & Q(user=request.user)) #q jest potrzebne na multiple filter conditions
    #     c.amount = c.amount + 1
    #     c.save()
    #     user = request.user #login
    #     basket = Basket.objects.filter(user=user) #wez basketinfo
    #     il = 0
    #     for i in basket:
    #             total = i.ilosc * i.product.cena
    #             il = il + total
    #     inTotal = il + 10
    #     print(prod_id)
    #     data={
    #         'ilosc': i.ilosc,
    #         'il': il,
    #         'total': inTotal
    #     }
    #     return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Basket.objects.filter(user=request.user))
        user=request.user
        adres=Client.objects.filter(user=user)
        basket = Basket.objects.filter(user=user)
        famount = 0
        for i in basket:
            value = i.amount * i.product.cena
            famount = famount + value
        totalcost = famount + 10
        razoramount = int(totalcost * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = {"amount":razoramount,"currency":"INR","receipt":"order_receiptid_12"}
        payment_response = client.order.create(data=data)
        print(payment_response)
        #{'id': 'order_KrK2rpDkhcWDYA', 'entity': 'order', 'amount': 18, 'amount_paid': 0, 'amount_due': 18, 'currency': 'USD', 'receipt': 'order_receiptid_12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1670918751}
        order_id = payment_response['id']
        print(order_id)
        order_status = payment_response['status']
        print(order_status)
        if order_status == 'created':
            platnosc = Payment(
                user=user,
                cena=totalcost,
                orderId = order_id,
                paymentStatus = order_status
            )
            platnosc.save()
        return render(request, 'app/checkout.html', locals())

@login_required
def orders(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Basket.objects.filter(user=request.user))
    order = Order.objects.filter(user=request.user)
    return render(request, 'app/orders.html', locals())

@login_required
def payment(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    #print("payment_done: orderid:", order_id,"paymentid: ", payment_id, "clientId=",client_id)

    user=request.user.id
    cze=request.user
    client=Client.objects.get(id=cust_id)
    print(cust_id)
    platnosc = Payment.objects.get(orderId=order_id)
    platnosc.oplacone = True
    platnosc.paymentId = payment_id
    platnosc.save()

    basket = Basket.objects.filter(user=user)
    for i in basket:
        Order(user=cze, client=client, product=i.product, ilosc=i.amount, platnosc=platnosc).save()
        i.delete()
    return redirect("orders")

@login_required
def search(request):
    pyt = request.GET['search']
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Basket.objects.filter(user=request.user))
    prod = Product.objects.filter(Q(nazwa__icontains=pyt))
    return render(request, "app/search.html", locals())
