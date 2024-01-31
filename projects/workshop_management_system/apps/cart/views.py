from django.shortcuts import render, redirect
from django.views import View
from . import madule, models
from django.http import Http404, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class CartView(View, LoginRequiredMixin):
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


class RemoveCourseView(View, LoginRequiredMixin):
    def get(self, request, slug):
        cart = madule.Cart(self.request)
        cart.remove(slug)
        total_price = cart.total_price()

        return JsonResponse({'response': 'ok', 'total_price': total_price})
