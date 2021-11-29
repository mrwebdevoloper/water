from django.shortcuts import render, redirect

from main.models import *
from django.views.generic import DetailView
from django.http import JsonResponse

def Home(request):
    context = {
        'product':Product.objects.all(),
        'blogs':Blog.objects.all(),
        'foydali':Foydali.objects.all(),
        'client':Clients.objects.all(),
    }
    return render(request, 'index.html', context)


def Blogs(request):
    return render(request, 'blog.html')

def About(request):
    return render(request, 'about.html')


class ProductDetail(DetailView) :
    model = Blog
    
    template_name = 'blog-details.html'
    context_object_name = 'blog'



def AddToCart(request, id):
    user = request.user

    try:
        shop = Shop.objects.create(client=user, status=0)
    except:
        shop = Shop.objects.create(client = user)
    product = Product.objects.get(id=id)
    if product.discount:
        ShopItem.objects.create(shop=shop, product=product, quantity=1, total=product.discount)
        shop.total += product.discount
    else:
        ShopItem.objects.create(shop=shop, product=product, quantity=1, total=product.price)
        shop.total += product.price
    shop.save()
    return redirect('/')


def Cart(request):
    shop = Shop.objects.filter(status=0)
    products = ShopItem.objects.filter(shop__client=request.user, shop__status=0 )
    context = {
        'products':products,
        'shop':shop[0],
    }
    return render (request, 'cart.html', context)

def CountSavatcha(request):
    count = ShopItem.objects.filter(shop__client=request.user, shop__status=0)
    s = 0
    for c in count:
        s += c.total

    data = {
        'count': count.count(),
        'total': s
    }


    return JsonResponse(data)

def BuyurtmaBerish(request, id):
    shop = Shop.objects.get(id=id)
    shop.status=1
    shop.save()

    return redirect('/')



def DeleteCart(request, id):

    item = ShopItem.objects.get(id=id)
    item.delete()


    return redirect('/cart/')
