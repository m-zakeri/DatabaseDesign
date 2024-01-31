from django.shortcuts import render, redirect
from django.views import View
from . import madule, models
from django.http import Http404, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = madule.Cart(self.request)
        if not cart.total_price():
            return render(request, 'cart/empty-cart.html')
        return render(request, 'cart/cart.html', {'cart': cart})

    def post(self, request):
        try:
            slug = request.POST.get('slug')
            course = models.Course.objects.get(slug=slug)
            cart = madule.Cart(self.request)
            cart.add(course)
            return redirect('cart_app:cart')
        except:
            raise Http404('course is not found.')


class RemoveCourseView(LoginRequiredMixin, View):
    def get(self, request, slug):
        cart = madule.Cart(self.request)
        cart.remove(slug)
        total_price = cart.total_price()

        return JsonResponse({'response': 'ok', 'total_price': total_price})


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        order = models.Order.objects.filter(id=id)
        if order.exists():
            return render(request, 'cart/checkout.html', {'order': order[0]})
        raise Http404('order is not found.')


class OrderCreationView(LoginRequiredMixin, View):
    def get(self, request):
        cart = madule.Cart(request)
        total_price = cart.total_price()
        order = models.Order.objects.create(customer=self.request.user.customer, total_price=total_price)
        for item in cart:
            models.OrderItem.objects.create(order_id=order.id, course=item['course'], final_price=item['price'])

        cart.remove_cart()
        return redirect('cart_app:order_detail', order.id)


class CouponView(View):
    def post(self, request, id):

        name_discount = request.POST.get('name_discount')
        output = madule.apply_coupon(request, name_discount, id)
        return JsonResponse({'text_message': output[0], 'final_price': output[1]})
