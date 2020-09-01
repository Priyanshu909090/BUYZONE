from math import ceil

from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Women, Men, Watch, Kids, Other, Shoes
from .models import Contact
from .models import Order


def index(request):
    # # product = Product.objects.all()
    # price = Product.objects.values('product_price', 'product_id')
    # price1 = {item['price'] for item in price}
    #
    # actualprice = Product.objects.values('actual_price', 'product_id')
    # actualprice1 = {item['actualprice'] for item in actualprice}
    # save1 = actualprice1 - price1

    allProd = []
    catprod = Product.objects.values('category')
    cats = {item['category'] for item in catprod}

    for cat in cats:
        product = Product.objects.filter(category=cat)
        # if product == 'T-shirt':
        n = len(product)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allProd.append([product, range(1, n), nSlide])

    params = {'allProd': allProd}
    return render(request, 'shop/index.html', params)


def contact(request):
    # contact = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        address = request.POST.get('address', )
        textarea = request.POST.get('textarea', )
        contact = Contact(name=name, email=email, phone=phone, address=address, textarea=textarea)
        contact.save()

    return render(request, 'shop/contact.html')


def productView(request, myid):
    product = Product.objects.filter(product_id=myid)

    param = {'product': product[0]}
    return render(request, 'shop/productView.html', param)


def cart(request):
    return render(request, 'shop/cart.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def about(request):
    return render(request, 'shop/about.html')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        address = request.POST.get('address', ) + " " + request.POST.get('address2', '')
        city = request.POST.get('city', )
        state = request.POST.get('state', )
        zip_code = request.POST.get('zip_code', )

        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()

        
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')


def category(request, womenid):
    ladiesproduct = Women.objects.filter(women_id=womenid)

    param = {'ladiesproduct': ladiesproduct[0]}
    return render(request, 'shop/category.html', param)


def women(request):
    allwomenProd = []
    womenprod = Women.objects.values('category')
    cats = {item['category'] for item in womenprod}

    for cat in cats:
        womenproduct = Women.objects.filter(category=cat)

        n = len(womenproduct)
        # nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allwomenProd.append([womenproduct, range(1, n)])

    params = {'allwomenProd': allwomenProd}

    return render(request, 'shop/women.html', params)


def womenview(request, wid):
    womenproduct = Women.objects.filter(women_id=wid)

    param = {'womenproduct': womenproduct[0]}
    return render(request, 'shop/women.html', param)


def men(request):
    allmenProd = []
    menprod = Men.objects.values('category')
    cats = {item['category'] for item in menprod}

    for cat in cats:
        menproduct = Men.objects.filter(category=cat)

        n = len(menproduct)
        # nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allmenProd.append([menproduct, range(1, n)])

    params = {'allmenProd': allmenProd}

    return render(request, 'shop/men.html', params)


def kid(request):
    allkidProd = []
    kidprod = Kids.objects.values('category')
    cats = {item['category'] for item in kidprod}

    for cat in cats:
        kidsproduct = Kids.objects.filter(category=cat)

        n = len(kidsproduct)
        # nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allkidProd.append([kidsproduct, range(1, n)])

    params = {'allkidProd': allkidProd}

    return render(request, 'shop/kid.html', params)


def other(request):
    allotherProd = []
    otherprod = Other.objects.values('category')
    cats = {item['category'] for item in otherprod}

    for cat in cats:
        otherproduct = Other.objects.filter(category=cat)

        n = len(otherproduct)
        # nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allotherProd.append([otherproduct, range(1, n)])

    params = {'allotherProd': allotherProd}
    return render(request, 'shop/other.html')


def shoe(request):
    allshoeProd = []
    shoeprod = Shoes.objects.values('category')
    cats = {item['category'] for item in shoeprod}

    for cat in cats:
        shoeproduct = Shoes.objects.filter(category=cat)

        n = len(shoeproduct)
        # nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allshoeProd.append([shoeproduct, range(1, n)])

    params = {'allshoeProd': allshoeProd}
    return render(request, 'shop/shoe.html')


def watch(request):
    allwatchProd = []
    watchprod = Watch.objects.values('category')
    cats = {item['category'] for item in watchprod}

    for cat in cats:
        watchproduct = Watch.objects.filter(category=cat)

        n = len(watchproduct)
        # nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allwatchProd.append([watchproduct, range(1, n)])

    params = {'allwatchProd': allwatchProd}
    return render(request, 'shop/watch.html')
