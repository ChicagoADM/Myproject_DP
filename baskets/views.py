from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from baskets.models import Basket
from baskets.utils import get_user_baskets

from baskets.models import Products


def cart_add(request):

    product_id = request.POST.get("product_id")

    product = Products.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
        baskets = Basket.objects.filter(
            session_key=request.session.session_key, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Basket.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)
    
    user_cart = get_user_baskets(request)
    cart_items_html = render_to_string(
        "baskets/includes/included_cart.html", {"baskets": user_cart}, request=request)

    response_data = {
        "message": "Товар добавлен! Для оформления заказа, перейдите в корзину! ",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)
            

def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    basket = Basket.objects.get(id=cart_id)

    basket.quantity = quantity
    basket.save()
    updated_quantity = basket.quantity

    basket = get_user_baskets(request)
    cart_items_html = render_to_string(
        "baskets/includes/included_cart.html", {"baskets": basket}, request=request)

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quaantity": updated_quantity,
    }

    return JsonResponse(response_data)



def cart_remove(request):
    
    cart_id = request.POST.get("cart_id")

    cart = Basket.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_baskets(request)
    cart_items_html = render_to_string(
        "baskets/includes/included_cart.html", {"baskets": user_cart}, request=request)

    response_data = {
        "message": "Товар удален из корзины",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)