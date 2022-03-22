from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView

from app.models import HomeBanner, LiveSaleSection, ShoppingX, TrendingDeals, Cart


class MainView(TemplateView):
    template_name = 'app/just_the_result.html'

class PostJsonListView(View):
    def get(self, *args, **kwargs):
        upper = kwargs.get('num_posts')
        lower = upper - 2
        posts = list(ShoppingX.objects.values()[lower:upper])
        posts_size = len(ShoppingX.objects.all())
        max_size = True if upper >= posts_size else False
        return JsonResponse({'data': posts, 'max': max_size}, safe=False)



class IndexView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homebanners'] = HomeBanner.objects.all()
        context['livesales'] = LiveSaleSection.objects.all()
        context['shopping'] = ShoppingX.objects.all()
        context['trending'] = TrendingDeals.objects.all()
        return context


# def product_detail(request):
#     return render(request, 'app/productdetail.html')

class SingleDetail(DetailView):
    model = ShoppingX
    template_name = 'app/productdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopping'] = ShoppingX.objects.all()
        return context

class TrendingDetailsView(DetailView):
    model = TrendingDeals
    template_name = 'app/latestproduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopping'] = ShoppingX.objects.all()
        return context

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product= ShoppingX.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

# class AddToCartView(TemplateView):
#     template_name = 'app/addtocart.html'


def show_card(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        shipping_amount = 70
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                temp = (p.quantity * p.product.discount)
                amount += temp
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
        else:
            return render(request, 'app/emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp = (p.quantity * p.product.discount)
            amount += temp

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp = (p.quantity * p.product.discount)
            amount += temp

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp = (p.quantity * p.product.discount)
            amount += temp

            data = {
                'amount': amount,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request):
    return render(request, 'app/mobile.html')


def login(request):
    return render(request, 'app/login.html')


def customerregistration(request):
    return render(request, 'app/customerregistration.html')


def checkout(request):
    return render(request, 'app/checkout.html')


# def index(request):
#     shopping=ShoppingX.objects.all()
#     return render(request,'app/serch.html', {'shopping':shopping})